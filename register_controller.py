from flask import render_template, request, redirect
from base import app
from base.com.vo import register_vo


@app.route('/register')
def register_user():
    # render_template('admin/register.html')
    try:
        name = request.args.get("reg_name")
        email = request.args.get("reg_mail")
        password = request.args.get("reg_pwd1")
        confirm_password = request.args.get("reg_pwd2")
        print(name, email, password)
        # if register_vo.registerVO.filter(email=email).exists():
        #     print('Email already registered')
        #     return redirect('/')
        # if password == confirm_password:
        #     insertdata = register_vo(name=name, email=email, password=password)
        #     insertdata.save()
        #     print("Account Created")
        #     return redirect('/')
        # else:
        #     print("Invalid Password")
        #     return redirect('/register')
    except Exception as ex:
        print("register route exception occurred>>>>>>>>>>", ex)
        return render_template('admin/register.html', ex=ex)
    return render_template('admin/register.html')

