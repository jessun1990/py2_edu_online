# coding: utf-8
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from .models import UserFav
# Create your views here.


class AddFavView(View):
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():
        # 用户未登录
            return JsonResponse({'status': 'fail', 'msg': u'用户未登录'})

        else:
            try:
                result_for_check = UserFav.objects.filter(user=request.user,
                                                          fav_id=int(fav_id),
                                                          fav_type=int(fav_type))
                if result_for_check:
                    result_for_check.delete()

                    return JsonResponse({'status': 'success', 'msg': u'取消收藏'})

                else:
                    if int(fav_type) > 0 and int(fav_id) > 0:
                        new_fav = UserFav()
                        new_fav.user = request.user
                        new_fav.fav_type = fav_type
                        new_fav.fav_id = fav_id
                        new_fav.save()

                        return JsonResponse({'status': 'success', 'msg': u'收藏成功'})

                    else:

                        return JsonResponse({'status': 'fail', 'msg': u'收藏失败'})

            except Exception as e:
                return JsonResponse({'status': 'fail', 'msg': u'收藏失败'})
