# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import View
import random
# new
from movie.models import Review, MovieInfo
from Cinema_Pages.models import DefaultRecom #, TopRecom

# old
# from .func import fuzzy_finder
# from .func import GetOtherInfo
# from .forms import ReviewForm
import MySQLdb

# 首页
def index(request):
    return render(request, 'index.html')

# 推荐函数，包括默认推荐和用户推荐
# 未做：协同过滤和用户登录后的推荐
def recommendForUser(request):

    # user = request.user
    # user_recommend_movies = None
    default_recommend_movies = DefaultRecom.objects.all()

    # if user.is_authenticated:
    #     # 如果用户已经登陆
    #     user_recommend_movies = TopRecom.objects.filter(user_id=user.id)
    #     # defautl和recommend随机选取5个， 同时避免了recommend不足5个的情况
    #     # 如果是新用户，则推荐默认的8部电影
    #     if user_recommend_movies.count() < 8:
    #         user_recommend_movies = default_recommend_movies
    # else:
    #     # 如果用户没有登陆
    user_recommend_movies = default_recommend_movies
    return user_recommend_movies


def sortAverating(val):
    return val[1]

def calDefaultRecomm(request):
    # 24部评分最高，24部最新
    # 这里或许应该在设立一个id功能来
    # 每一个example对应的导演、主演只有一个
    tmp_title_list = []
    title_list = []

    recom_tuple = []
    lim_len_rate = 48
    len_index_rate = 0
    lim_len_date = 24
    len_index_date = 0


    all_movieinfo_rate = MovieInfo.objects.all().order_by('-numrating')
    for movie in all_movieinfo_rate:
        if (lim_len_rate > len_index_rate):
            if (movie.moviename not in tmp_title_list):
                tmp_title_list.append(movie.moviename)
                recom_tuple.append((movie.moviename, movie.averating))
                len_index_rate += 1
            else:
                continue
        else:
            break

    recom_tuple.sort(key = sortAverating(), reverse = True)
    for i in range(0,len_index_date):
        title_list.append(recom_tuple[i][0])


    all_movieinfo = MovieInfo.objects.all().order_by('-releasedate')

    for movie in all_movieinfo:
        if (lim_len_date > len_index_date):
            if movie.moviename not in title_list:
                title_list.append(movie.moviename)
                len_index_date += 1
            else:
                continue
        else:
            break

    #将当前默认推荐删除
    DefaultRecom.objects.filter().delete()

    for mvname in title_list:
        defaultrecom = DefaultRecom()
        defaultrecom.movie = MovieInfo.objects.get(moviename=mvname)
        defaultrecom.save()


class Cinema_Pages_view(View):
    def get(self, request):
        user_recommend_movie = recommendForUser(request=request)
        movie_list = []
        for movie in user_recommend_movie:
            movie_list.append(movie)
        paginator = Paginator(movie_list, 24)
        page = request.GET.get('page')
        movies = paginator.get_page(page)

        return render(request, 'movie_display.html', {
            "commend_movie": movies
        })


def reCal_spark(request):
    pass

