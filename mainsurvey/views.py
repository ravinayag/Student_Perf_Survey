from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from django.core.mail import send_mail

cursor = connection.cursor()

def page2(request):
    if request.method == 'POST':
        family_size = request.POST.get('fam_no')
        if family_size is not None:
            family_size = int(family_size)
            family_size += 2
        mot_edu = request.POST.get('mot_edu')
        fat_edu = request.POST.get('fat_edu')
        mot_job = request.POST.get('mot_job')
        fat_job = request.POST.get('fat_job')
        school = request.POST.get('school')
        reason = request.POST.get('reason')
        acd = request.POST.get('acd')
        if acd == '__other_option__':
            acd = request.POST.get('acd1')
        edu_sp = request.POST.get('edu_sp')
        fam_sp = request.POST.get('fam_sp')
        stand = request.POST.get('stand')
        pred = request.POST.get('pred')
        sem_det = request.POST.get('sem_det')
        class_stu = request.POST.get('class_stu')
        eng = request.POST.get('eng')
        mat = request.POST.get('mat')
        concept = request.POST.get('concept')
        eng1_marks = request.POST.get('eng1_marks')
        eng2_marks = request.POST.get('eng2_marks')
        mat_marks = request.POST.get('mat_marks')
        soc_marks = request.POST.get('soc_marks')
        add = request.POST.get('add')
        science = request.POST.get('science')
        soci = request.POST.get('soci')
        sec_lang = request.POST.get('sec_lang')
        sec_lang_marks1 = request.POST.get('sec_lang_marks1')
        sec_lang_marks2 = request.POST.get('sec_lang_marks2')
        math_marks = request.POST.get('math_marks')
        comp_marks = request.POST.get('comp_marks')
        oth_sub1 = request.POST.get('oth_sub1')
        oth_sub_marks1 = request.POST.get('oth_sub_marks1')
        oth_sub2 = request.POST.get('oth_sub2')
        oth_sub_marks2 = request.POST.get('oth_sub_marks2')
        oth_sub3 = request.POST.get('oth_sub3')
        oth_sub_marks3 = request.POST.get('oth_sub_marks3')
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3')
        health = request.POST.get('health')
        travel = request.POST.get('travel')
        study_time = request.POST.get('study_time')
        free_time = request.POST.get('free_time')
        play = request.POST.get('play')
        skip = request.POST.get('skip')
        extra = request.POST.get('extra')
        spo = request.POST.get('spo')
        per = request.POST.get('per')
        act_time = request.POST.get('act_time')
        mail_id = request.POST.get('mail_id')
        cursor.execute("INSERT INTO answers VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',\
        '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',\
        '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(family_size,mot_edu,fat_edu,mot_job,fat_job,school,reason,acd,edu_sp,fam_sp,stand,pred,sem_det,class_stu,eng,mat,concept,eng1_marks,eng2_marks,mat_marks,soc_marks,add,science,soci,sec_lang,sec_lang_marks1,sec_lang_marks2,math_marks,comp_marks,oth_sub1,oth_sub_marks1,oth_sub2,oth_sub_marks2,oth_sub3,oth_sub_marks3,num1,num2,num3,health,travel,study_time,free_time,play,skip,extra,spo,per,act_time,mail_id))
        mail_subject = 'A new row inserted'
        message = 'A new row inserted'
        send_mail(
            mail_subject,
            message,
            'ravinayag@gmail.com',
            ['ravinayag@gmail.com'],
            fail_silently=True,
        )
        return redirect('thankyou')
    else:
        return render(request,'mainsurvey/main.html')


def thankyou(request):
    return render(request,'mainsurvey/done.html')
