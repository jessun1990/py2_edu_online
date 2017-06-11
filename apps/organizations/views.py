# coding: utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db.models import Count
from pure_pagination import Paginator, PageNotAnInteger

from operations.forms import UserAskForm
from operations.models import UserFav
from .models import Organization, CityDict
from courses.models import Course, Video, Chapter
# Create your views here.


class OrgListView(View):
    """
        机构列表页
    """
    def get(self, request):
        all_cities = CityDict.objects.all()
        all_orgs = Organization.objects.all()

        # test
        # any_org = Organization()
        # any_org.course_nums = any_org.get_course_nums()
        # any_org.save()

        hot_orgs = Organization.objects.all().order_by('-click_nums')[:3]

        # 筛选功能
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=city_id)
            city_id = int(city_id)

        org_type = request.GET.get('ct', '')
        if org_type:
            all_orgs = all_orgs.filter(org_type=org_type)

        # 排序功能
        sort_keyword = request.GET.get('sort', '')
        if sort_keyword == 'students':
            all_orgs = all_orgs.order_by('-student_nums')

        if sort_keyword == 'courses':
            # all_orgs = all_orgs.order_by('course_nums')
            all_orgs = all_orgs.annotate(nums=Count('course')).order_by('-nums')

        all_orgs_nums = all_orgs

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 3, request=request)
        all_orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_cities': all_cities,
            'all_orgs': all_orgs,
            'all_orgs_nums': all_orgs_nums,
            'city_id': city_id,
            'org_type': org_type,
            'sort_keyword': sort_keyword,
            'hot_orgs': hot_orgs,
            })

    def post(self, request):
        pass


class UserAskView(View):
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)

        if user_ask_form.is_valid():
            user_ask = user_ask_form.save(commit=True)
            return JsonResponse({'status': 'success', 'msg': u'信息发送成功'})
            
        else:
            return JsonResponse({'status': 'fail', 'msg': u'您填写的信息不合法'})


class OrgHomeView(View):
    """
        机构首页
    """
    def get(self, request, org_id):
        current_page = 'org_home'
        course_org = Organization.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:3]

        if request.user.is_authenticated():
            if UserFav.objects.filter(user=request.user, fav_id=int(org_id), fav_type=2):
               is_fav = True
            else:
                is_fav = False
        else:
            is_fav =False

        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'all_teachers': all_teachers,
            'course_org': course_org,
            'current_page': current_page,
            'is_fav': is_fav
        })

    def post(self, request):
        pass


class OrgHomeCourseView(View):
    """
        机构首页 - 机构课程
    """
    def get(self, request, org_id):
        current_page = 'org_course'
        course_org = Organization.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]

        if request.user.is_authenticated():
            if UserFav.objects.filter(user=request.user, fav_id=int(org_id), fav_type=2):
                is_fav = True
            else:
                is_fav = False
        else:
            is_fav =False

        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            'current_page': current_page,
            'is_fav': is_fav
        })

    def post(self, request):
        pass


class OrgHomeDescView(View):
    """
        机构首页 - 机构介绍
    """
    def get(self, request, org_id):
        current_page = 'org_desc'
        course_org = Organization.objects.get(id=int(org_id))

        if request.user.is_authenticated():
            if UserFav.objects.filter(user=request.user, fav_id=int(org_id), fav_type=2):
                is_fav = True
            else:
                is_fav = False
        else:
            is_fav =False
        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            'current_page': current_page,
            'is_fav': is_fav
        })

    def post(self, request):
        pass


class OrgHomeTeacherView(View):
    """
        机构首页 - 机构讲师
    """
    def get(self, request, org_id):
        current_page = 'org_teacher'
        course_org = Organization.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()[:3]
        if request.user.is_authenticated():
            if UserFav.objects.filter(user=request.user, fav_id=int(org_id), fav_type=2):
                is_fav = True
            else:
                is_fav = False
        else:
            is_fav =False

        return render(request, 'org-detail-teachers.html', {
            'course_org': course_org,
            'all_teachers': all_teachers,
            'current_page': current_page,
            'is_fav': is_fav
        })
