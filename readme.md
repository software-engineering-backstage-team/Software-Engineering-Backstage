###项目后台系统开发：
    1.  前端插图考虑服务器负载应以矢量图为佳。
    2.  前后端传送使用表单，注意csrf
    3.  关于数据库连接，统一使用
            'NAME': 'Software_engineering_backstage',
            'USER': 'root',
            'PASSWORD': 'Software_engineering',
    4.  关于协同开发，不能直接往master线push，使用dev线或个人线，
        推荐个人线开发后推向dev，最后协调上主线。
    5.  一部分用户信息在登录到主页后会保存在session中供小组或
        组织内其他开发小队使用，注意，改信息仅包括
                    request.session['user_is_login'] = True
                    request.session['user_codename'] = user.codename
                    request.session['user_nickname'] = user.nickname
                    request.session['user_department'] = user.department_id
                    request.session['user_grant'] = user.grant
        若后台组需要使用其他数据请使用数据库查询。
    6.  前端页面的编写使用bootstrap模板，希望出现新的简洁美观的用户页面。
    7.  关于后端核心功能，请clone后查看相关注释及项目开发文档。
    8.  系统开发需大家通力配合，请大家积极学习相关知识，参与项目开发讨论。
            一些链接：
                [django学习课程][1]
                [git学习][2]
                


  [1]: https://ke.qq.com/course/308515
  [2]: https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000