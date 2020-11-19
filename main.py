import sys
import RW_ACCOUNT
import MENU
import CATCH_PUBLIC_COURSE as pub
import CATCH_PLANNED_COURSE as plan
import CATCH_OUTPLANNED_COURSE as outplan
import CATCH_ENGLISH_COURSE as eng
import LOGIN
import time


def begin_catch_course():
    catch_course_dic = {
        "1": "计划内选课",
        "2": "英语拓展课",
        "3": "跨专业选课",
        "4": "公选课",
        "0": "返回主菜单"
    }
    catch_course_menu = MENU.MENU(catch_course_dic)
    catch_course_menu.print_list()
    while True:
        _key = input(">>>")
        if _key == "1":
            planned=plan.PlannedCourse(account)
            planned.run()
            catch_course_menu.print_list()
        elif _key == "2":
            english = eng.EnglishCourse(account)
            english.run()
            catch_course_menu.print_list()
        elif _key == "3":
            outplanned = outplan.OutPlannedCourse(account)
            outplanned.run()
            catch_course_menu.print_list()
        elif _key == "4":
            public = pub.PublicCourse(account)
            public.run()
            catch_course_menu.print_list()
        elif _key == "0":
            return
        else:
            print("请输入正确的数字")


if __name__ == "__main__":
    print("\033[1;36m       欢迎来到正方教务系统抢课助手\033[0m\n本程序主要自动登录+爬取课程信息+发送选课数据包进行抢课"
          "\n\033[1;31m第一次运行时记得先设置账号密码,之后运行就不需要设置了(存放在account.json中哦~)\033[0m")
    print("请花三秒钟看完上面的提示")
    time.sleep(3)
    init_dic = {
        "1": "设置账号密码",
        "2": "开始抢课",
        "0": "退出"
    }
    init_menu = MENU.MENU(init_dic)
    init_menu.print_list()
    while True:
        key = input(">>>")
        if key == "1":
            RW_ACCOUNT.set_account()
            init_menu.print_list()
        elif key == "2":
            account = LOGIN.Account()
            account.login()
            begin_catch_course()
            init_menu.print_list()
        elif key == "0":
            sys.exit()
        else:
            print("请输入正确的数字")
