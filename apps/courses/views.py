# coding: utf-8
from random import randint
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger

from courses.models import Course, Chapter, CourseResource
from operations.models import UserFav
# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')
        hot_courses = Course.objects.all().order_by('-student_nums')[:3]

        sort_keywords = request.GET.get('sort', "")
        if sort_keywords == 'hot':
            all_courses = all_courses.order_by('-click_nums')

        if sort_keywords == 'students':
            all_courses = all_courses.order_by('-student_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 9, request=request)
        all_courses = p.page(page)

        return render(request, 'course-list.html', {
            "all_courses": all_courses,
            "hot_courses": hot_courses,
            "sort_keywords": sort_keywords
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_org = course.course_org
        same_courses = Course.objects.filter(course_org=course_org)

        course_is_fav = False
        course_org_is_fav = False

        # 登录状态下，课程 和 机构 是否收藏
        if request.user.is_authenticated():
            if UserFav.objects.filter(user=request.user, fav_id=int(course_id), fav_type=1):
                course_is_fav = True
            if UserFav.objects.filter(user=request.user, fav_id=int(course_org.id), fav_type=3):
                course_org_is_fav = True

        # 相关课程推荐
        try:
            course_nums = same_courses.count()
            random_index = randint(0, course_nums - 1)
            related_course = same_courses[random_index]
        except Exception as e:
            related_course = course

        return render(request, 'course-detail.html', {
            "course": course,
            "course_org": course_org,
            "related_course": related_course,
            "course_is_fav": course_is_fav,
            "course_org_is_fav": course_org_is_fav,
        })


class CourseVideoView(View):
    def get(self, request,course_id):
        course = Course.objects.get(id=int(course_id))
        teacher = course.teacher
        resource = CourseResource.objects.get(course_id=int(course_id))
        chapters = Chapter.objects.filter(course_id=int(course_id))

        return render(request, 'course-video.html', {
            "course": course,
            "teacher": teacher,
            "resource": resource,
            "chapters": chapters,
        })
