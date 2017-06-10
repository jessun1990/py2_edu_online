# coding: utf-8
from django.shortcuts import render
from django .views.generic import View
from django.http import HttpResponse, JsonResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from operations.forms import UserAskForm
from operations.models import UserFav
from .models import Organization, CityDict
# Create your views here.


class OrgListView(View):
    """
        机构列表页
    """
    def get(self, request):
        all_cities = CityDict.objects.all()
        all_orgs = Organization.objects.all()

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
            all_orgs = all_orgs.order_by('-course_nums')

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


class OrgAddFavView(View):
    """
        机构首页 - 收藏机构
    """
    def get(self):
        pass

    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
            # 用户未登录
            return JsonResponse({'status': 'fail', 'msg': u'用户未登录'})

        else:
            # 用户已经登录
            try:
                result_for_check = UserFav.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))

                if result_for_check:
                    result_for_check.delete()
                    return JsonResponse({'status': 'success', 'msg': u'取消收藏'})

                else:
                    if int(fav_type > 0) and int(fav_id > 0):
                        new_org_fav = UserFav()
                        new_org_fav.user = request.user
                        new_org_fav.fav_type = fav_type
                        new_org_fav.fav_id = fav_id
                        new_org_fav.save()

                        return JsonResponse({'status': 'success', 'msg': u'收藏成功'})
                    else:
                        return JsonResponse({'status': 'fail', 'msg': u'收藏失败'})

            except Exception as e:
                return JsonResponse({'status': 'fail', 'msg': u'收藏失败'})

