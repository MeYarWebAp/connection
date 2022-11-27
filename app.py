#hkh -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 15:56:02 2022
@author: Hamed Khalili
"""
#####
import random
import pandas as pd
import sqlalchemy
import pymysql
from sqlalchemy import create_engine
import cryptography
import mysql.connector
import time
import base64
import streamlit as st
import pandas as pd
import json
import smtplib as s


common_meyar_percent=0.75

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 








json_str = json.dumps({'name': None})
json_str = r'''{"name": null, "age": null}'''

#import pickle as pkle
import os.path


message = """
__موضوعات__
"""
#st.set_page_config(layout = "wide") # optional
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('',['تماس با ما','درباره معیار','پایان جستجوی من در معیار'])
    if page=='درباره معیار':
        st.write("instagram.com/meyar")
        #st.write("")
        
    if page == 'تماس با ما':#
        st.write('meyarwebapp@meyr.ir')# 
    if page=='پایان جستجوی من در معیار':
        #pppp = st.button('پاک شدن ایمیل من از معیار', key="100007697690002")
        #if pppp:#
        q='آیا مطمئن هستید که می خواهید ایمیل خود را در معیار پاک کنید؟'
        a=['خیر','بله']
        n444444=st.selectbox(q,a,key=5624724)
        if n444444=='بله':
  
            num444444 = st.text_input('لطفا ایمیل خود را وارد کنید',key=984647832928) 
            if num444444:
                num444444=num444444.lower()
                @st.cache(suppress_st_warning=True)  
                @st.cache(allow_output_mutation=False)
                def sendpassD(email_1):
                    
    
                    email_sender="meyar.web.app@gmail.com"
                    password="agfkeaqajzqnfidv"
                    email_receiver=email_1
                    rrr=random.randint(1000000001, 9999999999)
                    subject="NoReply: Meyar Delete Password"
                    body=str(rrr)
                    try:
                        connection=s.SMTP('smtp.gmail.com',587)
                        connection.starttls()
                        connection.login(email_sender,password)
                        message="Subject:{}\n\n{}".format(subject,body)
                        connection.sendmail(email_sender,email_receiver,message)
                        connection.quit()
                    except s.SMTPException as error:
                        st.write("در برقراری ارتباط با ایمیل داده شده، مشکلی فنی وجود دارد")
                        st.stop()
                    return rrr
                spd=sendpassD(num444444)
                #st.write(spd)
                num000000 = st.number_input('لطفا پسورد ارسال شده به ایمیل خود را وارد کنید',key=6352898764252525,step=1)
                if num000000:
                    
                    if (num000000==spd):

                        
                        #@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None, "builtins.weakref":lambda _: None})

                        
                        
                        
                        def getPandasfromtabl (x):
                            x=x+1
                            engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
                            dbConnection= engine.connect()
                            return dbConnection
                        #pd.read_sql("select * from Mtable", dbConnection)
                        
                        exist = pd.read_sql("select * from F", getPandasfromtabl (1))
                        exist_2 = pd.read_sql("select * from M", getPandasfromtabl (1))
                        w1=num444444 in exist['id'].values
                        w2=num444444 in exist_2['id'].values
                        if w1:
                            ix=exist.loc[exist['id']==num444444].index.tolist()
                            exist=exist.drop(ix)
                            engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
                            for col in exist.columns:
                                exist[col] = exist[col].astype('string')
                            #exist.reset_index(drop=True)
                            exist.to_sql(con=engine, name='F', if_exists='replace', index=False)#
                            
                            st.write('درخواست با موفقیت انجام شد')
                        if w2:
                            ix=exist_2.loc[exist_2['id']==num444444].index.tolist()
                            exist_2=exist_2.drop(ix)
                            engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
                            for col in exist_2.columns:
                                exist_2[col] = exist_2[col].astype('string')
                            
                            exist_2.to_sql(con=engine, name='M', if_exists='replace', index=False)#
                            
                            st.write('درخواست با موفقیت انجام شد')

st.markdown("<h5 style='text-align: center;'>بسمه تعالی</h5>", unsafe_allow_html=True )
st.markdown("<h5 style='text-align: center;'> معیار، بر مبنای اعتماد بوده و کوششی برای محافظت از خانواده و ارزش هاست</h5>", unsafe_allow_html=True )




num0 = st.text_input('لطفا ایمیل خود را وارد کنید') 
while not num0:
        
        if 1==1:
                 st.stop()

filename = 'MeYar '





#@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None, "builtins.weakref":lambda _: None})

def getPandasfromtable (x):
    x=x+1
    engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
    dbConnection= engine.connect()
    return dbConnection  #  







  
num0=num0.lower()


                
                
@st.cache(suppress_st_warning=True)               
@st.cache(allow_output_mutation=False)
def sendpass(email_1):#
    
    email_sender="meyar.web.app@gmail.com"
    password="agfkeaqajzqnfidv"
    email_receiver=email_1
    rrr=random.randint(1000000001, 9999999999)
    subject="NoReply: Meyar Password"
    body=str(rrr)
    try:
        connection=s.SMTP('smtp.gmail.com',587)
        connection.starttls()
        connection.login(email_sender,password)
        message="Subject:{}\n\n{}".format(subject,body)
        connection.sendmail(email_sender,email_receiver,message)
        connection.quit()
    except s.SMTPException as error:
        st.write("در برقراری ارتباط با ایمیل داده شده، مشکلی فنی وجود دارد")
        st.stop()
    return rrr
sp=sendpass(num0)
#st.write(sp)
num00 = st.number_input('لطفا پسورد ارسال شده به ایمیل خود را وارد کنید',key=63524252525,step=1)

while not num00:
        
        if 1==1:
            
                 st.stop()

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True 
    else:
        return False

 
    
    






if (num00==sp):
    
    

    exii=  pd.read_sql("select * from M", getPandasfromtable (1))
    exi=   pd.read_sql("select * from F", getPandasfromtable (1))
    
    w1=num0 in exi['id'].values
    if w1:
        
        ex=exi.loc[exi['id']==num0]
        ix = exi.loc[exi['id']==num0].index.tolist()
        
    w2=num0 in exii['id'].values
    if w2:
        
        ex=exii.loc[exii['id']==num0]
        ix = exii.loc[exii['id']==num0].index.tolist()
        
    W=w1 or w2   
    
    st.markdown("<h3 style='text-align: center;'>معیارهای خود را برای انتخاب فرد مناسب خود وارد کنید</h3>", unsafe_allow_html=True )

    if W:
        st.markdown('<div style="text-align: center;color:Gray">معیارهای شما اکنون بر اساس داده هایی که تا کنون وارد کرده اید، تنظیم شده اند</div>', unsafe_allow_html=True)
        
    
    
    with st.expander("رشته تحصیلی او"):
        num3 ='خیر'   
        q='رشته تحصیلی یا مهارتی او، ترجیحا'
        a=['این معیار برای من اهمیت ویژه ای ندارد','شاخه مهندسی','شاخه هنری','شاخه پزشکی','شاخه ورزشی','علوم حوزوی','علوم انسانی']
        if W:
            g=ex.iloc[0]['c_major']
            #d=a.index(g)
            n3 = st.multiselect(q,a,eval(g))
        else:
            n3 = st.multiselect(q,a)
        if n3!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_major_det']
                d=a.index(g)
                num3 = st.selectbox(q,a, index=d,key="33333")
            else:
                num3 = st.selectbox(q, a, key="3")

                
                
        num10 ='خیر'
        q='تحصیلات او چگونه است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','دکترا','فوق لیسانس','لیسانس','دیپلم','دانشجو']
        if W:
            g=ex.iloc[0]['c_academic_level']

            n10 = st.multiselect(q,a, eval(g))
        else:
            n10 = st.multiselect(q,a)

            #n1 = st.selectbox(q,(این معیار برای من اهمیت ویژه ای ندارد','بایستی غنی و متمول باشند','متوسط به بالا باشند','اگر فقیرباشند نیزمشکلی ندارم'))
        if n10!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_academic_level_det']
                d=a.index(g)
                num10 = st.selectbox(q,a, index=d, key="101010")
            else:
                num10 = st.selectbox(q, a, key="10")            
                
    
        q="او علاقه ویژه ای به ادامه دادن تحصیل دارد" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_study']
            d=a.index(g)
            n1007 = st.selectbox(q,a, index=d)
        else:
            n1007 = st.selectbox(q,a)
    with st.expander("خانواده او"):
    
        num6 ='خیر' 
        q='شغل اعضای خانواده او ترجیحا'
        a=['این معیار برای من اهمیت ویژه ای ندارد','معلم','پزشک','بازاری','کارگر','آتش نشان','کشاورز','شغل های ورزشی','روزنامه نگار','مربوط به فناوری اطلاعات','آشپز','مربوط به قانون','خلبان','راننده','مهندس','مربوط به هنر','محقق','مربوط به فروش','بانکداری و مالی','مدیریتی','معمار',' نانوا','پاکبان','آرایشگر','پستچی','نظامی','عکاس','مشاور املاک','سوپرمارکت','مهماندار','کارمند','میوه فروش','بقال','رستوران دار','کارخانه دار','بازرگانی','طلافروش','فاقد شغل','شغل دولتی','شغل شخصی']

        if W:
            g=ex.iloc[0]['c_family_job']
            #d=a.index(g)
            n6 = st.multiselect(q,a, eval(g))
        else:
            n6 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n6:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_family_job_det']
                d=a.index(g)
                num6 = st.selectbox(q,a, index=d)
            else:
                num6 = st.selectbox(q, ('خیر','بله'), key="6")

        num1 ='خیر'
        q='وضع اقتصادی خانواده او چگونه است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','نسبتا خوب','متوسط به بالا','متوسط','نسبتا پایین']


        if W:
            g=ex.iloc[0]['c_family_wealth']
            d=a.index(g)
            n1 = st.selectbox(q,a, index=d)
        else:
            n1 = st.selectbox(q,a)

        if n1!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_family_wealth_det']
                d=a.index(g)
                num1 = st.selectbox(q,a, index=d, key="11111")
            else:
                num1 = st.selectbox(q, a, key="1")        

        num5000 ='خیر'


        q='خانواده او از لحاظ جمعیت'
        a=['این معیار برای من اهمیت ویژه ای ندارد','پرجمعیت','کم جمعیت','تک فرزند']


        if W:
            g=ex.iloc[0]['c_family_number']
            d=a.index(g)
            n5000 = st.selectbox(q,a, index=d)
        else:
            n5000 = st.selectbox(q,a)

        if n5000!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_family_number_det']
                d=a.index(g)
                num5000 = st.selectbox(q,a, index=d, key="50005000")
            else:
                num5000= st.selectbox(q, a, key="5000")
        q='اگر بدانید که یکی از اعضای نزدیک خانواده او تجربه اعتیاد داشته است'
        a=['خیلی از آشنایی با او ناامید میشوم','خیلی از آشنایی با او ناامید نمی شوم']
        if W:
            g=ex.iloc[0]['c_fd']
            d=a.index(g)
            n1003 = st.selectbox(q,a, index=d)
        else:
            n1003 = st.selectbox(q,a)


        num19 ='خیر'   
        q=' از نظر دینی خانواده او'
        a=['این معیار برای من اهمیت ویژه ای ندارد','اهل نماز و روزه و معتدل در دین است','بسیار مقید به رعایت جزییات  واجبات و تا حد وسع ، مستحبات است','معتقد است اما اهل تقید کامل به احکام دینی نیست']
        if W:
            g=ex.iloc[0]['c_beleifs']
            d=a.index(g)
            n19 = st.selectbox(q,a, index=d)
        else:
            n19 = st.selectbox(q,a)
        if n19!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_beleifs_det']
                d=a.index(g)
                num19 = st.selectbox(q,a, index=d,key="1919")
            else:
                num19 = st.selectbox(q, a, key="19")
        q='اگر بدانید که یکی از اعضای نزدیک خانواده او تجربه جدایی داشته است'
        a=['خیلی از آشنایی با او ناامید میشوم','خیلی از آشنایی با او ناامید نمی شوم']
        if W:
            g=ex.iloc[0]['c_fj']
            d=a.index(g)
            n1004 = st.selectbox(q,a, index=d)
        else:
            n1004 = st.selectbox(q,a)
    
    
    with st.expander("عقاید او"):
        num1002 ='خیر'
        q='از نظر سیاسی او چگونه است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','بسیار حساس به مسایل','کمتر حساس به مسایل']
        if W:
            g=ex.iloc[0]['c_politic']
            d=a.index(g)
            n1002 = st.selectbox(q,a, index=d)
        else:
            n1002 = st.selectbox(q,a)
        if n1002!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_politic_det']
                d=a.index(g)
                num1002 = st.selectbox(q,a, index=d, key="10021002")
            else:
                num1002 = st.selectbox(q, a, key="1002")

        num999 ='خیر'


        q="او علاقه ویژه ای به شرکت در مراسم  مذهبی دارد" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_din']
            d=a.index(g)
            n1008 = st.selectbox(q,a, index=d)
        else:
            n1008 = st.selectbox(q,a)
        q='در ماه مبارک رمضان او ... روزه می گیرد؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','گاهی','هر روز']
        if W:
            g=ex.iloc[0]['c_ramezan']
            d=a.index(g)
            n999 = st.selectbox(q,a, index=d)
        else:
            n999 = st.selectbox(q,a)
        if n999!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_ramezan_det']
                d=a.index(g)
                num999 = st.selectbox(q,a, index=d,key="99999999")
            else:
                num999 = st.selectbox(q, a, key="999999") 

        q="او مانوس به نماز و دعاست" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_doa']
            d=a.index(g)
            n1012 = st.selectbox(q,a, index=d)
        else:
            n1012 = st.selectbox(q,a)
      
        
        #q='Gender of head of household?'
        #num4 = st.selectbox(q, ('M','F'))
    with st.expander("ظاهر او"):
        q='حداقل سن او'
        if W:
            g=ex.iloc[0]['c_min_age']
            #st.write(g)
            #d=eval(a.index(g))
            num7 = st.slider(q, 0, 100, int(g))
        else:
            num7 = st.slider(q, 0, 100, 1)


        q='حداکثر سن او'
        if W:
            g=ex.iloc[0]['c_max_age']
            num8 = st.slider(q,0, 100, int(g))
        else:
            num8 = st.slider(q,0, 100, 1)

        q="او توجه ویژه ای به آراسته بودن ظاهر خود دارد" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_zaher']
            d=a.index(g)
            n1006 = st.selectbox(q,a, index=d)
        else:
            n1006 = st.selectbox(q,a)
        q='حداقل قد او'
        if W:
            g=ex.iloc[0]['c_hight_min']
            num11 = st.slider(q,0, 200, int(g))
        else:
            num11 = st.slider(q, 0, 200, 1)
        q='حداکثر قد او'
        if W:
            g=ex.iloc[0]['c_hight_max']
            num12 = st.slider(q,0, 200, int(g))
        else:
            num12 = st.slider(q,0, 200, 1)

        num13 ='خیر'
        q='چهره او'
        a=['این معیار برای من اهمیت ویژه ای ندارد','سیاه','سبزه','سفید']

        if W:
            g=ex.iloc[0]['c_face_color']
            n13= st.multiselect(q,a, eval(g))
        else:
            n13 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n13:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_face_det']
                d=a.index(g)
                num13 = st.selectbox(q,a, index=d, key= "1313")
            else:
                num13 = st.selectbox(q, ('خیر','بله'), key="13")  
        num14 ='خیر'
        q='وزن او'
        a= ['این معیار برای من اهمیت ویژه ای ندارد','لاغر','بسیارلاغر','متناسب','کمی چاق','چاق']
        if W:
            g=ex.iloc[0]['c_weight']
            n14= st.multiselect(q,a, eval(g))
        else:
            n14 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n14:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_weight_det']
                d=a.index(g)
                num14 = st.selectbox(q,a, index=d, key="1414")
            else:
                num14 = st.selectbox(q, ('خیر','بله'), key="14")  
        num15 ='خیر'
        q='بینی او'
        a=['این معیار برای من اهمیت ویژه ای ندارد','عمل نکرده است','کوچک','متناسب','نسبتا بزرگ']
        if W:
            g=ex.iloc[0]['c_nose']
            n15= st.multiselect(q,a, eval(g))
        else:
            n15 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n15:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_nose_det']
                d=a.index(g)
                num15 = st.selectbox(q,a, index=d,key="1515")
            else:
                num15 = st.selectbox(q, ('خیر','بله'), key="15")    


        num150 ='خیر'
        q='موی سر او'
        a=['این معیار برای من اهمیت ویژه ای ندارد','کم پشت','رشد تا موی بلند','متوسط']
        if W:
            g=ex.iloc[0]['c_hair']
            n150= st.multiselect(q,a, eval(g))
        else:
            n150 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n150:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_hair_det']
                d=a.index(g)
                num150 = st.selectbox(q,a, index=d,key="15105")
            else:
                num150 = st.selectbox(q, ('خیر','بله'), key="150")    



        num16 ='خیر'
        q='چشمان او'
        a=['این معیار برای من اهمیت ویژه ای ندارد','رنگی نیست',' رنگی است']
        if W:
            g=ex.iloc[0]['c_eyes']
            d=a.index(g)
            n16 = st.selectbox(q,a, index=d)
        else:
            n16= st.selectbox(q,a)
        if n16!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_eyes_det']
                d=a.index(g)
                num16 = st.selectbox(q,a, index=d,key="1616")
            else:
                num16 = st.selectbox(q, a, key="16")   
        num17 ='خیر'    
        q='دارای معلولیت'
        a=['این معیار برای من اهمیت ویژه ای ندارد','نیست']
        if W:
            g=ex.iloc[0]['c_disability']
            d=a.index(g)
            n17 = st.selectbox(q,a, index=d)
        else:
            n17= st.selectbox(q,a)
        if n17!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_disability_det']
                d=a.index(g)
                num17 = st.selectbox(q,a, index=d,key="1717")
            else:
                num17 = st.selectbox(q, a, key="17")    

        num7000 ='خیر'    
        q='دارای بیماری خاص'
        a=['این معیار برای من اهمیت ویژه ای ندارد','نیست']
        if W:
            g=ex.iloc[0]['c_des']
            d=a.index(g)
            n7000 = st.selectbox(q,a, index=d)
        else:
            n7000= st.selectbox(q,a)
        if n7000!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_des_det']
                d=a.index(g)
                num7000 = st.selectbox(q,a, index=d,key="1000717")
            else:
                num7000 = st.selectbox(q, a, key="10007")    
    #num3000 ='خیر'
    with st.expander("زندگی گذشته او"):
        q='اگر بدانید او پیش از این، ازدواج کرده است'
        a=['خیلی از آشنایی با او ناامید میشوم','خیلی از آشنایی با او ناامید نمی شوم']
        if W:
            g=ex.iloc[0]['c_eg']
            d=a.index(g)
            n3000 = st.selectbox(q,a, index=d)
        else:
            n3000= st.selectbox(q,a)

          
            
            


    with st.expander("برنامه های مشترک شما و او"):
        num20 ='خیر'
        q='مراسم ازدواج'
        a=['این معیار برای من اهمیت ویژه ای ندارد','حداقل در حد متوسط جامعه','بسیار ساده و حداقلی برگزار شود','ترجیحا برگزار نشود و مبلغ آن صرف زندگی شود','حتما بیشتر از سطح متوسط جامعه باشد','بسیار مجلل و شکیل']
        if W:
            g=ex.iloc[0]['c_marriage_exp']
            d=a.index(g)
            n20 = st.selectbox(q,a, index=d)
        else:
            n20 = st.selectbox(q,a)
        if n20!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_marriage_exp_det']
                d=a.index(g)
                num20 = st.selectbox(q,a, index=d,key="2020")
            else:
                num20 = st.selectbox(q, a, key="20")       

        num222 ='خیر'
        q='دور بودن از همدیگر به خاطر مسایل کاری تا چه میزان برایتان قابل تحمل است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','تا چند ماه','تا یک ماه','تا یک هفته']
        if W:
            g=ex.iloc[0]['c_dur']
            d=a.index(g)
            n222 = st.selectbox(q,a, index=d)
        else:
            n222 = st.selectbox(q,a)
        if n222!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_dur_det']
                d=a.index(g)
                num222 = st.selectbox(q,a, index=d,key="212221")
            else:
                num222 = st.selectbox(q, a, key="221")       



        num21 ='خیر'   
        q='فرزند آوری'
        a=['این معیار برای من اهمیت ویژه ای ندارد','ترجیحا فرزندان زیاد','ترجیحا فرزند کمتر','ترجیحا بدون فرزند آوری']
        if W:
            g=ex.iloc[0]['c_want_children']
            d=a.index(g)
            n21 = st.selectbox(q,a, index=d)
        else:
            n21 = st.selectbox(q,a)
        if n21!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_want_children_det']
                d=a.index(g)
                num21 = st.selectbox(q,a, index=d,key="2121")
            else:
                num21 = st.selectbox(q, a, key="21") 


        num2000='خیر'   
        q='از نظر محل زندگی دلخواه'
        a=['این معیار برای من اهمیت ویژه ای ندارد','ترجیحا خلوت و پر از طبیعت','ترجیحا شهر و پر از جنب و جوش']
        if W:
            g=ex.iloc[0]['c_il']
            d=a.index(g)
            n2000 = st.selectbox(q,a, index=d)
        else:
            n2000 = st.selectbox(q,a)
        if n2000!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_il_det']
                d=a.index(g)
                num2000 = st.selectbox(q,a, index=d,key="20002000")
            else:
                num2000 = st.selectbox(q, a, key="2000") 


        q="خریدن هدیه و کادو برای همدیگر در مناسبت ها" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_kadu']
            d=a.index(g)
            n2222 = st.selectbox(q,a, index=d)
        else:
            n2222 = st.selectbox(q,a)


        num6000 ='خیر'
        q='با هم به چگونه موسیقی ای گوش می دهید؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','موسیقی پاپ','نوای مذهبی','موسیقی هنری','موسیقی سنتی']
        if W:
            g=ex.iloc[0]['c_nava']
            n6000= st.multiselect(q,a, eval(g))
        else:
            n6000 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n6000:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_nava_det']
                d=a.index(g)
                num6000 = st.selectbox(q,a, index=d,key="6000")
            else:
                num6000 = st.selectbox(q, ('خیر','بله'), key="6000")    
    with st.expander("روش اقتصادی او"):  
        num1001 ='خیر'
        q='از نظر مالی او چگونه است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','بیشتر اهل خرج کردن','بیشتر اهل پس انداز کردن']
        if W:
            g=ex.iloc[0]['c_money']
            d=a.index(g)
            n1001 = st.selectbox(q,a, index=d)
        else:
            n1001 = st.selectbox(q,a)
        if n1001!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_money_det']
                d=a.index(g)
                num1001 = st.selectbox(q,a, index=d, key="10011001")
            else:
                num1001 = st.selectbox(q, a, key="1001")

        num213 ='خیر'
        q='او فردی هست که'
        a=['این معیار برای من اهمیت ویژه ای ندارد','گاهی وسایل خود را به راحتی به دوستان و آشنایان می بخشد','اصولا به سختی وسایل مربوط به خود را به کسی می بخشد']
        if W:
            g=ex.iloc[0]['c_bakh']
            d=a.index(g)
            n213 = st.selectbox(q,a, index=d)
        else:
            n213 = st.selectbox(q,a)

        if n213!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_bakh_det']
                d=a.index(g)
                num213 = st.selectbox(q,a, index=d,key="2221322")
            else:
                num213 = st.selectbox(q, a, key="213")
        num22 ='خیر'   
        q='  او مالک خانه'
        a=['این معیار برای من اهمیت ویژه ای ندارد','هست']
        if W:
            g=ex.iloc[0]['c_house_ownership']
            d=a.index(g)
            n22 = st.selectbox(q,a, index=d)
        else:
            n22= st.selectbox(q,a)
        if n22!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_house_ownership_det']
                d=a.index(g)
                num22 = st.selectbox(q,a, index=d,key="2222")
            else:
                num22 = st.selectbox(q, a, key="22") 
        num23 ='خیر'  
        q='او مالک اتومبیل'
        a=['این معیار برای من اهمیت ویژه ای ندارد','هست']
        if W:
            g=ex.iloc[0]['c_auto_ownership']
            d=a.index(g)
            n23 = st.selectbox(q,a, index=d)
        else:
            n23= st.selectbox(q,a)
        if n23!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_auto_ownership_det']
                d=a.index(g)
                num23 = st.selectbox(q,a, index=d,key="2323")
            else:
                num23 = st.selectbox(q, a, key="23")
        num24 ='خیر'   
        q=' او دارای شغل ثابت'
        a=['این معیار برای من اهمیت ویژه ای ندارد','هست']
        if W:
            g=ex.iloc[0]['c_employment']
            d=a.index(g)
            n24 = st.selectbox(q,a, index=d)
        else:
            n24= st.selectbox(q,a)
        if n24!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_employment_det']
                d=a.index(g)
                num24 = st.selectbox(q,a, index=d,key="2424")
            else:
                num24 = st.selectbox(q, a, key="24")
          
     
         
    with st.expander("طرز فکر و روش زندگی او"):
        num2 ='خیر'
        q='او خیلی به فلسفه و چرایی سوالات زندگی می اندیشد'
        a=['این معیار برای من اهمیت ویژه ای ندارد','خیر','بله']
        if W:
            g=ex.iloc[0]['c_philo']
            d=a.index(g)
            n2 = st.selectbox(q,a, index=d)
        else:
            n2 = st.selectbox(q,a)

        if n2!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_philo_det']
                d=a.index(g)
                num2 = st.selectbox(q,a, index=d,key="22222")
            else:
                num2 = st.selectbox(q, a, key="2")
    
    
        num313 ='خیر'
        q='نگاه او به آدم هایی که هنوز نمی شناسدشان'
        a=['این معیار برای من اهمیت ویژه ای ندارد','مشکوک','خوشبینانه']
        if W:
            g=ex.iloc[0]['c_negah']
            d=a.index(g)
            n313 = st.selectbox(q,a, index=d)
        else:
            n313 = st.selectbox(q,a)

        if n313!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_negah_det']
                d=a.index(g)
                num313 = st.selectbox(q,a, index=d,key="22223132")
            else:
                num313 = st.selectbox(q, a, key="2313")
    
    
        q='اگر بدانید او دارای وسواس در شستشو و نظافت است'
        a=['خیلی از آشنایی با او ناامید میشوم','خیلی از آشنایی با او ناامید نمی شوم']
        if W:
            g=ex.iloc[0]['c_vas']
            d=a.index(g)
            n8000 = st.selectbox(q,a, index=d)
        else:
            n8000= st.selectbox(q,a)
    
        num5 ='خیر'
        q='در برابر اشتباهات اطرافیان او'
        a=['این معیار برای من اهمیت ویژه ای ندارد','ترجیحا اهل مراعات','ترجیحا رک']

        if W:
            g=ex.iloc[0]['c_mistake']
            d=a.index(g)
            n5 = st.selectbox(q,a, index=d)
        else:
            n5 = st.selectbox(q,a)
        if n5!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_mistake_det']
                d=a.index(g)
                num5 = st.selectbox(q,a, index=d,key="55555")
            else:
                num5 = st.selectbox(q, a, key="5")
    
    
        num4 ='خیر'
        q='در کارهای روزمره او چگونه است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','خیلی اهل برنامه ریزی قبلی برای کارها','خیلی فرد خودجوش و تصمیم گیر در لحظه']
        if W:
            g=ex.iloc[0]['c_program']
            d=a.index(g)
            n4 = st.selectbox(q,a, index=d)
        else:
            n4 = st.selectbox(q,a)
        if n4!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_program_det']
                d=a.index(g)
                num4 = st.selectbox(q,a, index=d,key="44444")
            else:
                num4 = st.selectbox(q, a, key="4") 



        num413 ='خیر'
        q='او بیشتر وقت ها ... می ماند'
        a=['این معیار برای من اهمیت ویژه ای ندارد','ساکت و آرام','خوش صحبت و پر گفتگو']# a=['این معیار برای من اهمیت ویژه ای ندارد','مشکوک','خوشبینانه']
        if W:
            g=ex.iloc[0]['c_harf']
            d=a.index(g)
            n413 = st.selectbox(q,a, index=d)
        else:
            n413 = st.selectbox(q,a)

        if n413!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_harf_det']
                d=a.index(g)
                num413 = st.selectbox(q,a, index=d,key="41323132")
            else:
                num413 = st.selectbox(q, a, key="2341313")
    
        num18 ='خیر'
        q='از نظر اجتماعی او چگونه است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','متمایل به خلوت و ارتباط کم','علاقمند به بیرون رفتن و ارتباط']
        if W:
            g=ex.iloc[0]['c_social_att']
            n18= st.multiselect(q,a, eval(g))
        else:
            n18 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n18:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_social_att_det']
                d=a.index(g)
                num18 = st.selectbox(q,a, index=d,key="1818")
            else:
                num18 = st.selectbox(q, ('خیر','بله'), key="18")  
        num25 ='خیر'
        q='از نظر روحی او'
        a=['این معیار برای من اهمیت ویژه ای ندارد','بسیار صبور که در شرایط حساس، آرام باقی می ماند','بسیار احساسی که در شرایط حساس، زود به جوش می آید']
        if W:
            g=ex.iloc[0]['c_mental_att']
            n25= st.multiselect(q,a, eval(g))
        else:
            n25 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n25:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_mental_att_det']
                d=a.index(g)
                num25 = st.selectbox(q,a, index=d,key="2525")
            else:
                num25 = st.selectbox(q, ('خیر','بله'), key="25")
    
        q="این توانایی را دارد که محبت خود را به طور ویژه ای با کلام خود هم نشان می دهد" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_moh']
            d=a.index(g)
            n1009 = st.selectbox(q,a, index=d)
        else:
            n1009 = st.selectbox(q,a)   


        q="او به طور ویژه ای فرد شوخ طبعی است" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_humor']
            d=a.index(g)
            n1010 = st.selectbox(q,a, index=d)
        else:
            n1010 = st.selectbox(q,a)
        num9 ='خیر'
        q='محل زندگی او'
        a=['این معیار برای من اهمیت ویژه ای ندارد','اصفهان','اردبیل','آذربایجان غربی','آذربایجان شرقی','البرز','ایلام','بوشهر','تهران','چهارمحال و بختیاری','خراسان جنوبی','خراسان رضوی','خراسان شمالی','خوزستان','زنجان','سمنان','سیستان و بلوچستان','فارس','قزوین','قم','کردستان','کرمان','کرمانشاه','کهگیلویه و بویراحمد','گلستان','گیلان','لرستان','مازندران','مرکزی','هرمزگان','همدان','یزد']
        if W:
            g=ex.iloc[0]['c_living_location']
            n9= st.multiselect(q,a, eval(g))
        else:
            n9 = st.multiselect(q,a)
        if 'این معیار برای من اهمیت ویژه ای ندارد' not in n9:
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_living_location_det']
                d=a.index(g)
                num9 = st.selectbox(q,a, index=d, key="9999")
            else:
                num9 = st.selectbox(q, ('خیر','بله'), key="9")














        num1000 ='خیر'
        q='ورزش کردن او برای شما چقدر مهم است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','خیلی زیاد','خیلی کم']
        if W:
            g=ex.iloc[0]['c_sport']
            d=a.index(g)
            n1000 = st.selectbox(q,a, index=d)
        else:
            n1000 = st.selectbox(q,a)
        if n1000!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_sport_det']
                d=a.index(g)
                num1000 = st.selectbox(q,a, index=d, key="10001000")
            else:
                num1000 = st.selectbox(q, a, key="1000")  








        num1011 ='خیر'
        q='از نظر خلق و خو او چگونه است؟'
        a=['این معیار برای من اهمیت ویژه ای ندارد','فردی با آرامش بسیار','فردی با هیجان سرشار']
        if W:
            g=ex.iloc[0]['c_mood']
            d=a.index(g)
            n1011 = st.selectbox(q,a, index=d)
        else:
            n1011 = st.selectbox(q,a)
        if n1011!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_mood_det']
                d=a.index(g)
                num1011 = st.selectbox(q,a, index=d, key="10111011")
            else:
                num1011 = st.selectbox(q, a, key="1011")  








        q="او در غذا درست کردن مهارت ویژه ای دارد" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_food']
            d=a.index(g)
            n1005 = st.selectbox(q,a, index=d)
        else:
            n1005 = st.selectbox(q,a)











        q="او یک ساز موسیقی دارد" 
        a=['این معیار برای من اهمیت ویژه ای دارد','این معیار برای من اهمیت ویژه ای ندارد']
        if W:
            g=ex.iloc[0]['c_music']
            d=a.index(g)
            n1013 = st.selectbox(q,a, index=d)
        else:
            n1013 = st.selectbox(q,a)     














        num27 ='خیر'
        q='او گاهی سیگار می کشد'
        a=['این معیار برای من اهمیت ویژه ای ندارد','مشکل دارم']
        if W:
            g=ex.iloc[0]['c_smoke']
            d=a.index(g)
            n27 = st.selectbox(q,a, index=d)
        else:
            n27= st.selectbox(q,a)
        if n27!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_smoke_det']
                d=a.index(g)
                num27 = st.selectbox(q,a, index=d,key="2727")
            else:
                num27 = st.selectbox(q, a, key="27")        
        num28 ='خیر'
        q='او گاهی الکل مصرف می کند'
        a=('این معیار برای من اهمیت ویژه ای ندارد','مشکل دارم')
        if W:
            g=ex.iloc[0]['c_drink']
            d=a.index(g)
            n28 = st.selectbox(q,a, index=d)
        else:
            n28= st.selectbox(q,a)
        if n28!='این معیار برای من اهمیت ویژه ای ندارد':
            q='آیا پاسخ شما، معیاری قطعی برای شماست؟'
            a=['خیر','بله']
            if W:
                g=ex.iloc[0]['c_drink_det']
                d=a.index(g)
                num28 = st.selectbox(q,a, index=d,key="2828")
            else:
                num28 = st.selectbox(q, a, key="28")          
            
            
    
     
    st.markdown("<h3 style='text-align: center;'>ویژگی های مربوط به خودتان را وارد کنید</h3>", unsafe_allow_html=True )
    if W:
        st.markdown('<div style="text-align: center;color:Gray">ویژگی های شما اکنون بر اساس داده هایی که تا کنون وارد کرده اید، تنظیم شده اند</div>', unsafe_allow_html=True)
    with st.expander("ویژگی های شما"):
        q='جنسیت شما؟'
        a=['مرد','زن']
        if W:
            g=ex.iloc[0]['gender']
            d=a.index(g)
            n100 = st.selectbox(q,a, index=d,key="100100")
        else:
            n100 = st.selectbox(q, a, key="100")

        q='شغل اعضای درجه یک خانواده شما؟'
        a=['معلم','پزشک','بازاری','کارگر','آتش نشان','کشاورز','شغل های ورزشی','روزنامه نگار','مربوط به فناوری اطلاعات','آشپز','مربوط به قانون','خلبان','راننده','مهندس','مربوط به هنر','محقق','مربوط به فروش','بانکداری و مالی','مدیریتی','معمار',' نانوا','پاکبان','آرایشگر','پستچی','نظامی','عکاس','مشاور املاک','سوپرمارکت','مهماندار','کارمند','میوه فروش','بقال','رستوران دار','کارخانه دار','بازرگانی','طلافروش','فاقد شغل','شغل دولتی','شغل شخصی']

        if W:
            g=ex.iloc[0]['family_job']
            n106= st.multiselect(q,a, eval(g))
        else:
            n106 = st.multiselect(q,a)
        q=' سن شما؟'
        if W:
            g=ex.iloc[0]['age']
            num107 = st.slider(q,0, 100, int(g))
        else:
            num107 = st.slider(q, 0, 100, 1)
        q='خانواده شما از لحاظ مالی'
        a=['نسبتا خوب','متوسط به بالا','متوسط','نسبتا پایین']
        if W:
            g=ex.iloc[0]['family_wealth']
            d=a.index(g)
            n101 = st.selectbox(q,a, index=d)
        else:
            n101 = st.selectbox(q,a) 
        q='شما فردی هستید که خیلی به فلسفه و چرایی سوالات زندگی می اندیشید'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['philo']
            d=a.index(g)
            n102 = st.selectbox(q,a, index=d)
        else:
            n102 = st.selectbox(q,a) 
        q='محل زندگی شما'
        a=['اصفهان','اردبیل','آذربایجان غربی','آذربایجان شرقی','البرز','ایلام','بوشهر','تهران','چهارمحال و بختیاری','خراسان جنوبی','خراسان رضوی','خراسان شمالی','خوزستان','زنجان','سمنان','سیستان و بلوچستان','فارس','قزوین','قم','کردستان','کرمان','کرمانشاه','کهگیلویه و بویراحمد','گلستان','گیلان','لرستان','مازندران','مرکزی','هرمزگان','همدان','یزد']

        if W:
            g=ex.iloc[0]['living_location']
            d=a.index(g)
            n109= st.selectbox(q,a, index=d)
        else:
            n109 = st.selectbox(q,a)
        q='تحصیلات شما چگونه است؟'
        a=['دکترا','فوق لیسانس','لیسانس','دیپلم','دانشجو']
        if W:
            g=ex.iloc[0]['academic_level']
            #d=a.index(g)
            n110= st.multiselect(q,a, eval(g))
        else:
            n110 = st.multiselect(q,a)
        q=' قد شما'
        if W:
            g=ex.iloc[0]['hight']
            num111 = st.slider(q,0, 200, int(g))
        else:
            num111 = st.slider(q, 0, 200, 1)
        q=' چهره شما'
        a=['سیاه','سبزه','سفید']
        if W:
            g=ex.iloc[0]['face_color']
            d=a.index(g)
            num112= st.selectbox(q,a, index=d)
        else:
            num112 = st.selectbox(q,a)

        q='شما فردی هستید که'
        a=['گاهی وسایل خود را به راحتی به دوستان و آشنایان می بخشد','اصولا به سختی وسایل مربوط به خود را به کسی می بخشد']
        if W:
            g=ex.iloc[0]['bakh']
            d=a.index(g)
            n2130 = st.selectbox(q,a, index=d)
        else:
            n2130 = st.selectbox(q,a) 

        q=' وزن شما'
        a=['لاغر','بسیارلاغر','متناسب','کمی چاق','چاق']
        if W:
            g=ex.iloc[0]['weight']
            d=a.index(g)
            num113= st.selectbox(q,a, index=d)
        else:
            num113 = st.selectbox(q,a)
        q=' بینی شما'
        a=['عمل نکرده است','کوچک','متناسب','نسبتا بزرگ']#a=['این معیار برای من اهمیت ویژه ای ندارد','کم پشت','رشد تا موی بلند','متوسط']
        if W:
            g=ex.iloc[0]['nose']
            num114= st.multiselect(q,a, eval(g))
        else:
            num114 = st.multiselect(q,a)
        q=' چشمان شما'
        a=('رنگی نیست','رنگی است')
        if W:
            g=ex.iloc[0]['eyes']
            d=a.index(g)
            num115= st.selectbox(q,a, index=d)
        else:
            num115 = st.selectbox(q,a)




        q='موی سر شما'
        a=['کم پشت','رشد تا موی بلند','متوسط']
        if W:
            g=ex.iloc[0]['hair']
            d=a.index(g)
            num1500= st.selectbox(q,a, index=d)
        else:
            num1500 = st.selectbox(q,a)

        q=' آیا گاهی سیگار می کشید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['smoke']
            d=a.index(g)
            num127= st.selectbox(q,a, index=d)
        else:
            num127 = st.selectbox(q,a)
        #a=['این معیار برای من اهمیت ویژه ای ندارد','ساکت و آرام','خوش صحبت و پر گفتگو']# a=['این معیار برای من اهمیت ویژه ای ندارد','مشکوک','خوشبینانه']
        q='نگاه شما به آدم هایی که هنوز نمی شناسیدشان'
        a=['مشکوک','خوشبینانه']
        if W:
            g=ex.iloc[0]['negah']
            d=a.index(g)
            n3130 = st.selectbox(q,a, index=d)
        else:
            n3130 = st.selectbox(q,a)
        q='شما بیشتر وقت ها ... می مانید'
        a=['ساکت و آرام','خوش صحبت و پر گفتگو']
        if W:
            g=ex.iloc[0]['harf']
            d=a.index(g)
            n4130 = st.selectbox(q,a, index=d)
        else:
            n4130 = st.selectbox(q,a)
        q=' آیا گاهی الکل مصرف می کنید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['drink']
            d=a.index(g)
            num128= st.selectbox(q,a, index=d)
        else:
            num128 = st.selectbox(q,a)
        q=' آیا دارای هرگونه بیماری خاص هستید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['des']
            d=a.index(g)
            num70000= st.selectbox(q,a, index=d)
        else:
            num70000 = st.selectbox(q,a)

        q='در ماه مبارک رمضان  شما روزه می گیرید؟'
        a=['گاهی' ,'هر روز']
        if W:
            g=ex.iloc[0]['ramezan']
            d=a.index(g)
            num9999= st.selectbox(q,a, index=d)
        else:
            num9999 = st.selectbox(q,a)


        q=' آیا دارای هرگونه معلولیت هستید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['disability']
            d=a.index(g)
            num116= st.selectbox(q,a, index=d)
        else:
            num116 = st.selectbox(q,a)

        q='رشته تحصیلی یا مهارتی شما'
        a=['شاخه مهندسی','شاخه هنری','شاخه پزشکی','شاخه ورزشی','علوم حوزوی','علوم انسانی']
        if W:
            g=ex.iloc[0]['major']
            d=a.index(g)
            n103= st.selectbox(q,a, index=d)
        else:
            n103 = st.selectbox(q,a) 
        q='خانواده شما از لحاظ جمعیت'
        a=['پرجمعیت','کم جمعیت','تک فرزند']
        if W:
            g=ex.iloc[0]['family_number']
            d=a.index(g)
            n50000= st.selectbox(q,a, index=d)
        else:
            n50000 = st.selectbox(q,a)
        q='پیش از این ازدواج کرده اید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['eg']
            d=a.index(g)
            n30000= st.selectbox(q,a, index=d)
        else:
            n30000 = st.selectbox(q,a)




        q='شما در کارهای روزمره چگونه هستید؟ '
        a=['خیلی اهل برنامه ریزی قبلی برای کارها','خیلی فرد خودجوش و تصمیم گیر در لحظه']
        if W:
            g=ex.iloc[0]['program']
            d=a.index(g)
            n104= st.selectbox(q,a, index=d)
        else:
            n104 = st.selectbox(q,a) 
        q='شما در مقابل اشتباهات دیگران چگونه هستید؟ '
        a=['ترجیحا اهل مراعات','ترجیحا رک']
        if W:
            g=ex.iloc[0]['mistake']
            d=a.index(g)
            n105= st.selectbox(q,a, index=d)
        else:
            n105 = st.selectbox(q,a) 
        q=' از نظر اجتماعی شما چگونه هستید؟'
        a=['متمایل به خلوت و ارتباط کم','علاقمند به بیرون رفتن و ارتباط']
        if W:
            g=ex.iloc[0]['social_att']
            num118= st.multiselect(q,a, eval(g))
        else:
            num118 = st.multiselect(q,a)
        q=' از نظر  روحی شما فردی هستید'
        a=['بسیار صبور که در شرایط حساس، آرام باقی می ماند','بسیار احساسی که در شرایط حساس، زود به جوش می آید']
        if W:
            g=ex.iloc[0]['mental_att']
            num119= st.multiselect(q,a, eval(g))
        else:
            num119 = st.multiselect(q,a)
        q='خانواده شما'
        a=['اهل نماز و روزه و معتدل در دین است','بسیار مقید به رعایت جزییات  واجبات و تا حد وسع ، مستحبات است','معتقد است اما اهل تقید کامل به احکام دینی نیست']
        if W:
            g=ex.iloc[0]['beleifs']
            d=a.index(g)
            num120= st.selectbox(q,a, index=d)
        else:
            num120 = st.selectbox(q,a)
        q='شما مالک خانه هستید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['house_ownership']
            d=a.index(g)
            n121= st.selectbox(q,a, index=d)
        else:
            n121 = st.selectbox(q,a) 
        q='شما مالک اتومبیل هستید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['auto_ownership']
            d=a.index(g)
            n122= st.selectbox(q,a, index=d)
        else:
            n122 = st.selectbox(q,a) 

        q='آیا شما دارای وسواس در شستشو و نظافت هستید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['vas']
            d=a.index(g)
            num80000= st.selectbox(q,a, index=d)
        else:
            num80000 = st.selectbox(q,a)


        q='شما چقدر ورزش می کنید؟'
        a=['خیلی زیاد',' خیلی کم']
        if W:
            g=ex.iloc[0]['sport']
            d=a.index(g)
            n10000= st.selectbox(q,a, index=d)
        else:
            n10000 = st.selectbox(q,a)     

        q='از نظر مالی شما چگونه هستید؟'
        a=['بیشتر اهل خرج کردن','بیشتر اهل پس انداز کردن']
        if W:
            g=ex.iloc[0]['money']
            d=a.index(g)
            n10001= st.selectbox(q,a, index=d)
        else:
            n10001 = st.selectbox(q,a)  



        q='از نظر سیاسی شما چگونه هستید؟'
        a=['بسیار حساس به مسایل',' کمتر حساس به مسایل']
        if W:
            g=ex.iloc[0]['politic']
            d=a.index(g)
            n10002= st.selectbox(q,a, index=d)
        else:
            n10002 = st.selectbox(q,a)  


        q='یکی از اعضای نزدیک خانواده شما تجربه اعتیاد داشته است؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['fd']
            d=a.index(g)
            n10003= st.selectbox(q,a, index=d)
        else:
            n10003 = st.selectbox(q,a)

        q='از نظر خلق و خو شما چگونه فردی هستید؟'
        a=['فردی با آرامش بسیار','فردی با هیجان سرشار']
        if W:
            g=ex.iloc[0]['mood']
            d=a.index(g)
            num10011= st.selectbox(q,a, index=d)
        else:
            num10011 = st.selectbox(q,a)


        q='یکی از اعضای نزدیک خانواده شما تجربه جدایی داشته است؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['fj']
            d=a.index(g)
            n10004= st.selectbox(q,a, index=d)
        else:
            n10004 = st.selectbox(q,a)

        q='شما در غذا درست کردن مهارت ویژه ای دارید؟'
        a=['بله','خیر']
        if W:
            g=ex.iloc[0]['food']
            d=a.index(g)
            n10005= st.selectbox(q,a, index=d)
        else:
            n10005 = st.selectbox(q,a)    

        q='شما توجه ویژه ای به آراسته بودن ظاهر خود دارید؟'
        a=['بله','خیر']
        if W:
            g=ex.iloc[0]['zaher']
            d=a.index(g)
            n10006= st.selectbox(q,a, index=d)
        else:
            n10006 = st.selectbox(q,a)       

        q='شما توجه ویژه ای به ادامه دادن تحصیل خود دارید؟'
        a=['بله','خیر']
        if W:
            g=ex.iloc[0]['study']
            d=a.index(g)
            n10007= st.selectbox(q,a, index=d)
        else:
            n10007 = st.selectbox(q,a) 

        q='شما توجه ویژه ای به شرکت در مراسم  مذهبی دارید؟'
        a=['بله','خیر']
        if W:
            g=ex.iloc[0]['din']
            d=a.index(g)
            n10008= st.selectbox(q,a, index=d)
        else:
            n10008 = st.selectbox(q,a) 


        q='شما این توانایی را دارید که محبت خود را به طور ویژه ای با کلام خود هم نشان می دهید '
        a=['بله','خیر']
        if W:
            g=ex.iloc[0]['moh']
            d=a.index(g)
            n10009= st.selectbox(q,a, index=d)
        else:
            n10009 = st.selectbox(q,a) 

        q='شما به طور ویژه ای فرد شوخ طبعی هستید'
        a=['بله','خیر']
        if W:
            g=ex.iloc[0]['humor']
            d=a.index(g)
            n10010= st.selectbox(q,a, index=d)
        else:
            n10010 = st.selectbox(q,a) 
        q='شما مانوس به نماز و دعا هستید'
        a=['بله','خیر']
        if W:
            g=ex.iloc[0]['doa']
            d=a.index(g)
            n10012= st.selectbox(q,a, index=d)
        else:
            n10012 = st.selectbox(q,a) 
        q='شما دارای سازموسیقی هستید'
        a=['بله','خیر']
        if W:
            g=ex.iloc[0]['music']
            d=a.index(g)
            n10013= st.selectbox(q,a, index=d)
        else:
            n10013 = st.selectbox(q,a) 
        q='شما دارای شغل ثابت هستید؟'
        a=['خیر','بله']
        if W:
            g=ex.iloc[0]['employment']
            d=a.index(g)
            n123= st.selectbox(q,a, index=d)
        else:
            n123 = st.selectbox(q,a) 
    st.markdown("<h3 style='text-align: center;'>معرفی گزینه ها</h3>", unsafe_allow_html=True )
    
    q='حد اقل درصد همپوشانی گزینه ها با معیارهای شما'
    if W:
        g=ex.iloc[0]['degree']
        num8765 = st.slider(q,0.75, 0.95, float(g),step=0.01)
    else:
        num8765 = st.slider(q,0.75, 0.95, 0.75,step=0.01)
    
    p = st.button('معرفی کن', key="10478502")

    if not p:
        st.stop()


    
    hisher_basket=[]
    my_basket=[]
    if p:
        
        existing_2= pd.read_sql("select * from M", getPandasfromtable (1))
        existing=   pd.read_sql("select * from F", getPandasfromtable (1))

        if W:

                if w1:
                    existing=existing.drop(ix)
                    #st.write(1111111111111111111)
                    if n100 != ex.iloc[0]['gender']:
                        
                        engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
                        existing.to_sql(con=engine, name='F', if_exists='replace', index=False)
                if w2:
                    existing_2=existing_2.drop(ix)
                    #st.write(22222222222222222222)
                    if n100 != ex.iloc[0]['gender']:
                        
                        engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
                        existing_2.to_sql(con=engine, name='M', if_exists='replace', index=False)

        if n100 !='مرد':
            
            df_1=pd.DataFrame({'id': [num0], 'gender':[n100],'degree':[num8765],'c_kadu':[n2222],'c_hair':[n150],'c_hair_det':[num150],'hair':[num1500],'c_negah':[n313],'c_negah_det':[num313],'negah':[n3130],'c_harf':[n413],'c_harf_det':[num413],'harf':[n4130],'c_bakh':[n213],'c_bakh_det':[num213],'bakh':[n2130],'c_dur':[n222],'c_dur_det':[num222],'c_ramezan':[n999],'c_ramezan_det':[num999],'ramezan':[num9999],'c_vas':[n8000],'vas':[num80000],'c_des':[n7000],'c_des_det':[num7000],'des':[num70000],'c_nava':[n6000],'c_nava_det':[num6000],'c_doa':[n1012],'c_music':[n1013],'doa':[n10012],'music':[n10013],'c_family_number':[n5000],'c_family_number_det':[num5000],'family_number':[n50000],'c_humor':[n1010],'humor':[n10010],'c_eg':[n3000],'eg':[n30000],'c_il':[n2000],'c_il_det':[num2000],'c_mood':[n1011],'c_mood_det':[num1011],'mood':[num10011],'c_moh':[n1009],'moh':[n10009],'c_food':[n1005],'food':[n10005],'c_zaher':[n1006],'zaher':[n10006],'c_study':[n1007],'study':[n10007],'c_din':[n1008],'din':[n10008],'c_sport':[n1000],'c_sport_det':[num1000],'sport':[n10000],'c_money':[n1001],'c_money_det':[num1001],'money':[n10001],'c_politic':[n1002],'c_politic_det':[num1002],'politic':[n10002],'c_fd':[n1003],'fd':[n10003],'c_fj':[n1004],'fj':[n10004],'c_min_age':[num7],'c_max_age':[num8],'c_family_wealth':[n1],'c_family_wealth_det':[num1],'c_philo':[n2],'c_philo_det':[num2],'c_living_location':[n9],'c_living_location_det':[num9],'c_academic_level':[n10],'c_academic_level_det':[num10],'c_hight_min':[num11],'c_hight_max':[num12],'c_face_color':[n13],'c_face_det':[num13],'c_weight':[n14], 'c_weight_det':[num14],'c_nose':[n15], 'c_nose_det':[num15],'c_eyes':[n16],'c_eyes_det':[num16],'c_smoke':[n27],'c_smoke_det':[num27],'c_drink':[n28],'c_drink_det':[num28],'c_disability':[n17],'c_disability_det':[num17],'c_major':[n3],'c_major_det':[num3],'c_program':[n4],'c_program_det':[num4], 'c_mistake':[n5], 'c_mistake_det':[num5],'c_social_att':[n18],'c_social_att_det':[num18], 'c_mental_att':[n25],'c_mental_att_det':[num25],'c_beleifs':[n19],'c_beleifs_det':[num19],'c_house_ownership':[n22],'c_house_ownership_det':[num22],'c_auto_ownership':[n23],'c_auto_ownership_det':[num23],'c_employment':[n24],'c_employment_det':[num24],'c_marriage_exp':[n20], 'c_marriage_exp_det':[num20],'c_want_children':[n21],'c_want_children_det':[num21],'c_family_job':[n6],'c_family_job_det':[num6],  'family_job':[n106],'age':[num107],'family_wealth':[n101] ,'philo':[n102],'living_location':[n109],'academic_level':[n110] ,'hight':[num111], 'face_color':[num112],'weight':[num113] ,'nose':[num114] ,'eyes':[num115] ,'smoke':[num127] ,'drink':[num128] ,'disability':[num116] ,'major':[n103] ,'program':[n104] ,'mistake':[n105] ,'social_att':[num118] ,'mental_att':[num119] ,'beleifs':[num120] ,'house_ownership':[n121] ,'auto_ownership':[n122],'employment':[n123] ,'marriage_exp':[n20] ,'want_children':[n21],'candidate_list':[[['M',0]]]})        

            existing = existing.append(df_1)###
            for col in existing.columns:
                existing[col] = existing[col].astype('string')
            engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
            
            existing.to_sql(con=engine, name='F', if_exists='replace', index=False)#
            
        if n100 =='مرد':
            

            df_2=pd.DataFrame({'id': [num0], 'gender':[n100],'degree':[num8765],'c_kadu':[n2222],'c_hair':[n150],'c_hair_det':[num150],'hair':[num1500],'c_negah':[n313],'c_negah_det':[num313],'negah':[n3130],'c_harf':[n413],'c_harf_det':[num413],'harf':[n4130],'c_bakh':[n213],'c_bakh_det':[num213],'bakh':[n2130],'c_dur':[n222],'c_dur_det':[num222],'c_ramezan':[n999],'c_ramezan_det':[num999],'ramezan':[num9999],'c_vas':[n8000],'vas':[num80000],'c_des':[n7000],'c_des_det':[num7000],'des':[num70000],'c_nava':[n6000],'c_nava_det':[num6000],'c_doa':[n1012],'c_music':[n1013],'doa':[n10012],'music':[n10013],'c_family_number':[n5000],'c_family_number_det':[num5000],'family_number':[n50000],'c_humor':[n1010],'humor':[n10010],'c_eg':[n3000],'eg':[n30000],'c_il':[n2000],'c_il_det':[num2000],'c_mood':[n1011],'c_mood_det':[num1011],'mood':[num10011],'c_moh':[n1009],'moh':[n10009],'c_food':[n1005],'food':[n10005],'c_zaher':[n1006],'zaher':[n10006],'c_study':[n1007],'study':[n10007],'c_din':[n1008],'din':[n10008],'c_sport':[n1000],'c_sport_det':[num1000],'sport':[n10000],'c_money':[n1001],'c_money_det':[num1001],'money':[n10001],'c_politic':[n1002],'c_politic_det':[num1002],'politic':[n10002],'c_fd':[n1003],'fd':[n10003],'c_fj':[n1004],'fj':[n10004],'c_min_age':[num7],'c_max_age':[num8],'c_family_wealth':[n1],'c_family_wealth_det':[num1],'c_philo':[n2],'c_philo_det':[num2],'c_living_location':[n9],'c_living_location_det':[num9],'c_academic_level':[n10],'c_academic_level_det':[num10],'c_hight_min':[num11],'c_hight_max':[num12],'c_face_color':[n13],'c_face_det':[num13],'c_weight':[n14], 'c_weight_det':[num14],'c_nose':[n15], 'c_nose_det':[num15],'c_eyes':[n16],'c_eyes_det':[num16],'c_smoke':[n27],'c_smoke_det':[num27],'c_drink':[n28],'c_drink_det':[num28],'c_disability':[n17],'c_disability_det':[num17],'c_major':[n3],'c_major_det':[num3],'c_program':[n4],'c_program_det':[num4], 'c_mistake':[n5], 'c_mistake_det':[num5],'c_social_att':[n18],'c_social_att_det':[num18], 'c_mental_att':[n25],'c_mental_att_det':[num25],'c_beleifs':[n19],'c_beleifs_det':[num19],'c_house_ownership':[n22],'c_house_ownership_det':[num22],'c_auto_ownership':[n23],'c_auto_ownership_det':[num23],'c_employment':[n24],'c_employment_det':[num24],'c_marriage_exp':[n20], 'c_marriage_exp_det':[num20],'c_want_children':[n21],'c_want_children_det':[num21],'c_family_job':[n6],'c_family_job_det':[num6],  'family_job':[n106],'age':[num107],'family_wealth':[n101] ,'philo':[n102],'living_location':[n109],'academic_level':[n110] ,'hight':[num111], 'face_color':[num112],'weight':[num113] ,'nose':[num114] ,'eyes':[num115] ,'smoke':[num127] ,'drink':[num128] ,'disability':[num116] ,'major':[n103] ,'program':[n104] ,'mistake':[n105] ,'social_att':[num118] ,'mental_att':[num119] ,'beleifs':[num120] ,'house_ownership':[n121] ,'auto_ownership':[n122],'employment':[n123] ,'marriage_exp':[n20] ,'want_children':[n21],'candidate_list':[[['M',0]]]})        
            existing_2 = existing_2.append(df_2)###
            for col in existing_2.columns:
                existing_2[col] = existing_2[col].astype('string')
            
            engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
            
            existing_2.to_sql(con=engine, name='M', if_exists='replace', index=False)#
            


        if n100 =='مرد':
            
            
            
            e_1=pd.read_sql("select * from F", getPandasfromtable (1))
            le_1=len(e_1)

            basket=[]
            for i in range(0, le_1):
                treffer=0

                evc1=e_1.iloc[i]['age']
                if float(evc1)< float(num7) or float(evc1)>float(num8):
                    continue 
                if float(evc1)>=float(num7) and float(evc1)<=float(num8):
                    treffer=treffer+1
                evc2=e_1.iloc[i]['family_wealth']
                if n1=='این معیار برای من اهمیت ویژه ای ندارد':#a=['این معیار برای من اهمیتی ندارد','نسبتا خوب','متوسط به بالا','متوسط','نسبتا پایین']
                    treffer=treffer+1
                if n1!='این معیار برای من اهمیت ویژه ای ندارد':
                    if n1=='نسبتا خوب':
                        if num1=='بله':
                          if evc2!= 'نسبتا خوب':
                            continue
                          if evc2== 'نسبتا خوب':
                            treffer=treffer+1
                        if num1=='خیر':
                          if evc2== 'نسبتا خوب':
                            treffer=treffer+1
                    if n1=='متوسط به بالا': 
                        if num1=='بله':
                          if evc2==  'متوسط' or evc2==  'نسبتا پایین':
                            continue
                          if evc2==  'نسبتا خوب' or evc2== 'متوسط به بالا':
                            treffer=treffer+1
                        if num1=='خیر':
                          if evc2==  'نسبتا خوب' or evc2== 'متوسط به بالا':
                            treffer=treffer+1
                    if n1=='متوسط':
                        if num1=='بله':
                            if evc2== 'نسبتا پایین':
                                continue
                            if evc2==  'نسبتا خوب' or evc2== 'متوسط به بالا' or evc2=='متوسط' :
                                treffer=treffer+1
                        if num1=='خیر':
                            if evc2==  'نسبتا خوب' or evc2== 'متوسط به بالا' or evc2=='متوسط' :
                                treffer=treffer+1
                    if n1== 'نسبتا پایین':
                        treffer=treffer+1
                evc3=e_1.iloc[i]['philo'] 
                if n2=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                else:
                    if num2=='بله':
                        if n2!=evc3:
                            continue
                        else:
                            treffer=treffer+1
                    if num2=='خیر':
                        if n2==evc3:
                            treffer=treffer+1

                evc4=e_1.iloc[i]['living_location'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n9:
                    treffer=treffer+1
                else:
                    if num9=='بله':
                        if evc4 not in n9:
                            continue
                        if evc4 in n9:
                            treffer=treffer+1
                    if num9=='خیر':  
                        if evc4 in n9:
                            treffer=treffer+1
                evc5=e_1.iloc[i]['academic_level'] #['دکترا','فوق لیسانس','لیسانس','دیپلم','دانشجو']
                evc_5=[]
                if 'دکترا' in evc5:
                    evc_5.append('دکترا')
                    evc_5.append('فوق لیسانس')
                    evc_5.append('لیسانس')
                    evc_5.append('دیپلم')
                if 'فوق لیسانس' in evc5:
                    evc_5.append('فوق لیسانس')
                    evc_5.append('لیسانس')
                    evc_5.append('دیپلم')
                    
                if 'لیسانس' in evc5:
                    evc_5.append('لیسانس')
                    evc_5.append('دیپلم')
                #st.write(evc_5)
                #st.write(n10)
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n10:
                    treffer=treffer+1
                else:  
                    if num10=='بله':
                        if common_member(evc_5,n10)==False:
                            continue
                        else: 
                            treffer=treffer+1
                    if num10=='خیر':
                        if common_member(evc_5,n10): 
                            treffer=treffer+1
                evc6=e_1.iloc[i]['hight'] 
                if float(evc6)< float(num11) or float(evc6)>float(num12):
                    continue 
                if float(evc6)>=float(num11) and float(evc6)<=float(num12):
                    treffer=treffer+1
                evc7=e_1.iloc[i]['face_color'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n13:
                    treffer=treffer+1
                else:  
                    if num13=='بله':
                        if evc7 not in n13:
                            continue
                        if evc7 in n13:
                            treffer=treffer+1
                    if num13=='خیر':  
                        if evc7 in n13:
                            treffer=treffer+1
                evc8=e_1.iloc[i]['weight'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n14:
                    treffer=treffer+1
                else:  
                    if num14=='بله':
                        if evc8 not in n14:
                            continue
                        if evc8 in n14:
                            treffer=treffer+1
                    if num14=='خیر':  
                        if evc8 in n14:
                            treffer=treffer+1
                evc9=e_1.iloc[i]['nose'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n15:
                    treffer=treffer+1
                else:  
                    if num15=='بله':
                        if common_member(evc9,n15)==False :
                            continue
                        else:
                            treffer=treffer+1
                    if num15=='خیر':  
                        if evc9 in n15:
                            treffer=treffer+1
                evc10=e_1.iloc[i]['eyes']    
                if n16=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n16!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num16=='بله':
                        if evc10 != n16:
                            continue
                        if evc10 == n16:
                            treffer=treffer+1
                    if num16=='خیر':  
                        if evc10 == n16:
                            treffer=treffer+1
                evc11=e_1.iloc[i]['smoke']
                if n27=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n27!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num27=='بله':
                        if evc11=='بله':
                            continue
                        if evc11=='خیر':       
                             treffer=treffer+1
                    if num27=='خیر': 
                        if evc11=='خیر':       
                             treffer=treffer+1
                evc12=e_1.iloc[i]['drink']  
                if n28=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n28!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num28=='بله':
                        if evc12=='بله':
                            continue
                        if evc12=='خیر':       
                             treffer=treffer+1
                    if num28=='خیر': 
                        if evc12=='خیر':       
                             treffer=treffer+1
                evc13=e_1.iloc[i]['disability'] 
                if n17=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n17!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num17=='بله':
                        if evc13=='بله':
                            continue
                        if evc13=='خیر':       
                             treffer=treffer+1
                    if num17=='خیر': 
                        if evc13=='خیر':       
                             treffer=treffer+1
                evc14=e_1.iloc[i]['major'] #if issub(n25,evc18)== False:
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n3:
                    treffer=treffer+1
                else:
                    if num3=='بله':
                        if evc14 not in n3:
                            continue
                        else:       
                             treffer=treffer+1
                    if num3=='خیر': 
                        if evc14 in n3:       
                             treffer=treffer+1                    
                evc15=e_1.iloc[i]['program'] 
                if n4=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n4!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num4=='بله':
                        if evc15!=n4:
                            continue
                        else:       
                             treffer=treffer+1
                    if num4=='خیر': 
                        if evc15==n4:       
                             treffer=treffer+1 
                evc16=e_1.iloc[i]['mistake'] 
                if n5=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n5!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num5=='بله':
                        if evc16!=n5:
                            continue
                        else:       
                             treffer=treffer+1
                    if num5=='خیر': 
                        if evc16==n5:       
                             treffer=treffer+1  
                evc17=e_1.iloc[i]['social_att']
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n18:

                    treffer=treffer+1
                else:  
                    if num18=='بله':
                        if common_member(evc17,n18)== False :
                            continue
                        else:
                            treffer=treffer+1
                    if num18=='خیر':  
                        if common_member(evc17,n18):
                            treffer=treffer+1
                evc18=e_1.iloc[i]['mental_att']
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n25:

                    treffer=treffer+1
                else:  
                    if num25=='بله':
                        if common_member(evc18,n25)== False :
                            continue
                        else:
                            treffer=treffer+1
                    if num25=='خیر':  
                        if common_member(evc18,n25):
                            treffer=treffer+1
                evc19=e_1.iloc[i]['beleifs']
                if n19=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n19!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num19=='بله':
                        if n19!=evc19:
                            continue
                        if n19==evc19:
                            treffer=treffer+1
                    if num19=='خیر':  
                        if evc19==n19:
                            treffer=treffer+1 
                evc20=e_1.iloc[i]['house_ownership']

                if n22=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n22!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num22=='بله':
                        if evc20=='بله':
                            treffer=treffer+1
                        if evc20=='خیر':       
                             continue
                    if num22=='خیر': 
                         if evc20=='بله':     
                             treffer=treffer+1             
                evc21=e_1.iloc[i]['auto_ownership']

                if n23=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n23!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num23=='بله':
                        if evc21=='بله':
                            treffer=treffer+1
                        if evc21=='خیر':       
                             continue
                    if num23=='خیر': 
                         if evc21=='بله':     
                             treffer=treffer+1   
                evc22=e_1.iloc[i]['employment']

                if n24=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n24!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num24=='بله':
                        if evc22=='بله':
                            treffer=treffer+1
                        if evc22=='خیر':       
                             continue
                    if num24=='خیر': 
                         if evc22=='بله':     
                             treffer=treffer+1   
                evc23=e_1.iloc[i]['marriage_exp']           
                if n20=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n20!='این معیار برای من اهمیت ویژه ای ندارد':

                    if num20=='بله':
                        if n20!=evc23:
                            continue
                        if n20==evc23:
                            treffer=treffer+1
                    if num20=='خیر':  
                        if evc23==n20:
                            treffer=treffer+1  
                evc24=e_1.iloc[i]['want_children']           
                if n21=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n21!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num21=='بله':
                        if n21!=evc24:
                            continue
                        if n21==evc24:
                            treffer=treffer+1
                    if num21=='خیر':  
                        if evc24==n21:
                            treffer=treffer+1             
                evc25=e_1.iloc[i]['family_job'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n6:
                    treffer=treffer+1
                else:  
                    if num6=='بله':
                        if common_member(evc25,n6)==False :
                            continue
                        else:
                            treffer=treffer+1
                    if num6=='خیر':  
                        if evc25 in n6:
                            treffer=treffer+1           
                evc26=e_1.iloc[i]['sport']           
                if n1000=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n1000!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num1000=='بله':
                        if n1000!=evc26:
                            continue
                        if n1000==evc26:
                            treffer=treffer+1
                    if num1000=='خیر':  
                        if evc26==n1000:
                            treffer=treffer+1 
                evc27=e_1.iloc[i]['money']           
                if n1001=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n1001!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num1001=='بله':
                        if n1001!=evc27:
                            continue
                        if n1001==evc27:
                            treffer=treffer+1
                    if num1001=='خیر':  
                        if evc27==n1001:
                            treffer=treffer+1 
                evc28=e_1.iloc[i]['politic']           
                if n1002=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n1002!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num1002=='بله':
                        if n1002!=evc28:
                            continue
                        if n1002==evc28:
                            treffer=treffer+1
                    if num1002=='خیر':  
                        if evc28==n1002:
                            treffer=treffer+1 



                evc29=e_1.iloc[i]['fd']    
                if n1003=='خیلی از آشنایی با او ناامید میشوم':  
                    if evc29=='بله':
                        continue
                    else:
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                
                evc30=e_1.iloc[i]['fj']    
                if n1004=='خیلی از آشنایی با او ناامید میشوم':  
                    if evc30=='بله':
                        continue
                    else:
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc31=e_1.iloc[i]['food']    
                if n1005=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc31=='بله':
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc32=e_1.iloc[i]['zaher']    
                if n1006=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc32=='بله':
                        treffer=treffer+1   
                else:
                    treffer=treffer+1
                evc33=e_1.iloc[i]['study']    
                if n1007=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc33=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc34=e_1.iloc[i]['din']    
                if n1008=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc34=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc35=e_1.iloc[i]['moh']    
                if n1009=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc35=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc36=e_1.iloc[i]['humor']    
                if n1010=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc36=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc37=e_1.iloc[i]['mood']
                if n1011=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n1011!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num1011=='بله':
                        if n1011 != evc37:
                            continue
                        else:
                            treffer=treffer+1
                    if num1011=='خیر':  
                        if n1011 == evc37:
                            treffer=treffer+1
                evc38=e_1.iloc[i]['c_il']           
                if n2000=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n2000!='این معیار برای من اهمیت ویژه ای ندارد':

                    if num2000=='بله':
                        if n2000!=evc38:
                            continue
                        if n2000==evc38:
                            treffer=treffer+1
                    if num2000=='خیر':  
                        if evc38==n2000:
                            treffer=treffer+1 
                evc39=e_1.iloc[i]['eg'] 
                    
                if n3000=='خیلی از آشنایی با او ناامید میشوم':  
                    if evc39=='بله':
                        continue
                    else:
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc40=e_1.iloc[i]['family_number']
                if n5000=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n5000!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num5000=='بله':
                        if n5000 != evc40:
                            continue
                        else:
                            treffer=treffer+1
                    if num5000=='خیر':  
                        if n5000 == evc40:
                            treffer=treffer+1
                evc41=e_1.iloc[i]['doa']    
                if n1012=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc41=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc42=e_1.iloc[i]['music']    
                if n1013=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc42=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc43=e_1.iloc[i]['c_nava']
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n6000:

                    treffer=treffer+1
                else:  
                    if num6000=='بله':
                        if common_member(n6000,evc43)== False :
                            continue
                        else:
                            treffer=treffer+1
                    if num6000=='خیر':  
                        if common_member(n6000,evc43):
                            treffer=treffer+1
                evc44=e_1.iloc[i]['des'] 
                if n7000=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n7000!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num7000=='بله':
                        if evc44=='بله':
                            continue
                        if evc44=='خیر':       
                             treffer=treffer+1
                    if num7000=='خیر': 
                        if evc44=='خیر':       
                             treffer=treffer+1
                evc45=e_1.iloc[i]['vas']    
                if n8000=='خیلی از آشنایی با او ناامید میشوم':  
                    if evc45=='بله':
                        continue
                    else:
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc46=e_1.iloc[i]['ramezan'] 
                if n999=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n999!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num999=='بله':
                        if evc46!=n999:
                            continue
                        else:       
                             treffer=treffer+1
                    if num999=='خیر': 
                        if evc46==n999:       
                             treffer=treffer+1  
                evc47=e_1.iloc[i]['c_dur']           
                if n222=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n222!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num222=='بله':
                        if n222!=evc47:
                            continue
                        else:
                            treffer=treffer+1
                    if num222=='خیر':  
                        if evc47==n222:
                            treffer=treffer+1 
                evc48=e_1.iloc[i]['bakh'] 
                if n213=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                else:
                    if num213=='بله':
                        if n213!=evc48:
                            continue
                        else:
                            treffer=treffer+1
                    if num213=='خیر':
                        if n213==evc48:
                            treffer=treffer+1
                evc49=e_1.iloc[i]['negah'] 
                if n313=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                else:
                    if num313=='بله':
                        if n313!=evc49:
                            continue
                        else:
                            treffer=treffer+1
                    if num313=='خیر':
                        if n313==evc49:
                            treffer=treffer+1
                evc50=e_1.iloc[i]['harf'] 
                if n413=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                else:
                    if num413=='بله':
                        if n413!=evc50:
                            continue
                        else:
                            treffer=treffer+1
                    if num413=='خیر':
                        if n413==evc50:
                            treffer=treffer+1
                evc51=e_1.iloc[i]['hair'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n150:
                    treffer=treffer+1
                else:  
                    if num150=='بله':
                        if evc51 not in n150:
                            continue
                        if evc51 in n150:
                            treffer=treffer+1
                    if num150=='خیر':  
                        if evc51 in n150:
                            treffer=treffer+1
                evc52=e_1.iloc[i]['c_kadu']    
                if n2222=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc52==n2222:
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                if treffer/52>=num8765:
                    candidate=[e_1.iloc[i]['id'],treffer/52]
                    basket.append(candidate) #


                    li=eval(e_1.iloc[i]['candidate_list'])
                    #edited_li=[]
                    #st.write(li)
                    for j in li:
                        #st.write(j)
                        if j[0]== num0:
                            #edited_li.append([j[0],j[1]])
                            hisher_basket.append([j[0],j[1]])
                            my_basket.append(candidate)
                    #hisher_basket.append(edited_li)
                    #my_basket.append(candidate)
            #exii = get_as_dataframe(worksheet2 )
            exii=pd.read_sql("select * from M", getPandasfromtable (1))
                #exi.loc['id', 'candidate_list'] = str(basket)
            exii.loc[exii['id']==num0, ['candidate_list']] = str(basket)
            exii=exii.applymap(str)
                
            engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
            
            exii.to_sql(con=engine, name='M', if_exists='replace', index=False)
            






        if n100 !='مرد':
            
            
            e_2=pd.read_sql("select * from M", getPandasfromtable (1))
            le_2=len(e_2)
            basket=[]
            for i in range(0, le_2):
                treffer=0

                evc1=e_2.iloc[i]['age']
                if float(evc1)< float(num7) or float(evc1)>float(num8):
                    continue 
                if float(evc1)>=float(num7) and float(evc1)<=float(num8):
                    treffer=treffer+1
                evc2=e_2.iloc[i]['family_wealth']
                if n1=='این معیار برای من اهمیت ویژه ای ندارد':#a=['این معیار برای من اهمیتی ندارد','نسبتا خوب','متوسط به بالا','متوسط','نسبتا پایین']
                    treffer=treffer+1
                if n1!='این معیار برای من اهمیت ویژه ای ندارد':
                    if n1=='نسبتا خوب':
                        if num1=='بله':
                          if evc2!= 'نسبتا خوب':
                            continue
                          if evc2== 'نسبتا خوب':
                            treffer=treffer+1
                        if num1=='خیر':
                          if evc2== 'نسبتا خوب':
                            treffer=treffer+1
                    if n1=='متوسط به بالا': 
                        if num1=='بله':
                          if evc2==  'متوسط' or evc2==  'نسبتا پایین':
                            continue
                          if evc2==  'نسبتا خوب' or evc2== 'متوسط به بالا':
                            treffer=treffer+1
                        if num1=='خیر':
                          if evc2==  'نسبتا خوب' or evc2== 'متوسط به بالا':
                            treffer=treffer+1
                    if n1=='متوسط':
                        if num1=='بله':
                            if evc2== 'نسبتا پایین':
                                continue
                            if evc2==  'نسبتا خوب' or evc2== 'متوسط به بالا' or evc2=='متوسط' :
                                treffer=treffer+1
                        if num1=='خیر':
                            if evc2==  'نسبتا خوب' or evc2== 'متوسط به بالا' or evc2=='متوسط' :
                                treffer=treffer+1
                    if n1== 'نسبتا پایین':
                        treffer=treffer+1
                evc3=e_2.iloc[i]['philo'] 
                if n2=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                else:
                    if num2=='بله':
                        if n2!=evc3:
                            continue
                        else:
                            treffer=treffer+1
                    if num2=='خیر':
                        if n2==evc3:
                            treffer=treffer+1

                evc4=e_2.iloc[i]['living_location'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n9:
                    treffer=treffer+1
                else:
                    if num9=='بله':
                        if evc4 not in n9:
                            continue
                        if evc4 in n9:
                            treffer=treffer+1
                    if num9=='خیر':  
                        if evc4 in n9:
                            treffer=treffer+1
                evc5=e_2.iloc[i]['academic_level'] #['دکترا','فوق لیسانس','لیسانس','دیپلم','دانشجو']
                evc_5=[]
                if 'دکترا' in evc5:
                    evc_5.append('دکترا')
                    evc_5.append('فوق لیسانس')
                    evc_5.append('لیسانس')
                    evc_5.append('دیپلم')
                if 'فوق لیسانس' in evc5:
                    evc_5.append('فوق لیسانس')
                    evc_5.append('لیسانس')
                    evc_5.append('دیپلم')
                    
                if 'لیسانس' in evc5:
                    evc_5.append('لیسانس')
                    evc_5.append('دیپلم')
                #st.write(evc_5)
                #st.write(n10)
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n10:
                    treffer=treffer+1
                else:  
                    if num10=='بله':
                        if common_member(evc_5,n10)==False:
                            continue
                        else: 
                            treffer=treffer+1
                    if num10=='خیر':
                        if common_member(evc_5,n10): 
                            treffer=treffer+1
                evc6=e_2.iloc[i]['hight'] 
                if float(evc6)< float(num11) or float(evc6)>float(num12):
                    continue 
                if float(evc6)>=float(num11) and float(evc6)<=float(num12):
                    treffer=treffer+1
                evc7=e_2.iloc[i]['face_color'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n13:
                    treffer=treffer+1
                else:  
                    if num13=='بله':
                        if evc7 not in n13:
                            continue
                        if evc7 in n13:
                            treffer=treffer+1
                    if num13=='خیر':  
                        if evc7 in n13:
                            treffer=treffer+1
                evc8=e_2.iloc[i]['weight'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n14:
                    treffer=treffer+1
                else:  
                    if num14=='بله':
                        if evc8 not in n14:
                            continue
                        if evc8 in n14:
                            treffer=treffer+1
                    if num14=='خیر':  
                        if evc8 in n14:
                            treffer=treffer+1
                evc9=e_2.iloc[i]['nose'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n15:
                    treffer=treffer+1
                else:  
                    if num15=='بله':
                        if common_member(evc9,n15)==False :
                            continue
                        else:
                            treffer=treffer+1
                    if num15=='خیر':  
                        if evc9 in n15:
                            treffer=treffer+1
                evc10=e_2.iloc[i]['eyes']    
                if n16=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n16!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num16=='بله':
                        if evc10 != n16:
                            continue
                        if evc10 == n16:
                            treffer=treffer+1
                    if num16=='خیر':  
                        if evc10 == n16:
                            treffer=treffer+1
                evc11=e_2.iloc[i]['smoke']
                if n27=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n27!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num27=='بله':
                        if evc11=='بله':
                            continue
                        if evc11=='خیر':       
                             treffer=treffer+1
                    if num27=='خیر': 
                        if evc11=='خیر':       
                             treffer=treffer+1
                evc12=e_2.iloc[i]['drink']  
                if n28=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n28!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num28=='بله':
                        if evc12=='بله':
                            continue
                        if evc12=='خیر':       
                             treffer=treffer+1
                    if num28=='خیر': 
                        if evc12=='خیر':       
                             treffer=treffer+1
                evc13=e_2.iloc[i]['disability'] 
                if n17=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n17!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num17=='بله':
                        if evc13=='بله':
                            continue
                        if evc13=='خیر':       
                             treffer=treffer+1
                    if num17=='خیر': 
                        if evc13=='خیر':       
                             treffer=treffer+1
                evc14=e_2.iloc[i]['major'] #if issub(n25,evc18)== False:
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n3:
                    treffer=treffer+1
                else:
                    if num3=='بله':
                        if evc14 not in n3:
                            continue
                        else:       
                             treffer=treffer+1
                    if num3=='خیر': 
                        if evc14 in n3:       
                             treffer=treffer+1                    
                evc15=e_2.iloc[i]['program'] 
                if n4=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n4!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num4=='بله':
                        if evc15!=n4:
                            continue
                        else:       
                             treffer=treffer+1
                    if num4=='خیر': 
                        if evc15==n4:       
                             treffer=treffer+1 
                evc16=e_2.iloc[i]['mistake'] 
                if n5=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n5!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num5=='بله':
                        if evc16!=n5:
                            continue
                        else:       
                             treffer=treffer+1
                    if num5=='خیر': 
                        if evc16==n5:       
                             treffer=treffer+1  
                evc17=e_2.iloc[i]['social_att']
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n18:

                    treffer=treffer+1
                else:  
                    if num18=='بله':
                        if common_member(evc17,n18)== False :
                            continue
                        else:
                            treffer=treffer+1
                    if num18=='خیر':  
                        if common_member(evc17,n18):
                            treffer=treffer+1
                evc18=e_2.iloc[i]['mental_att']
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n25:

                    treffer=treffer+1
                else:  
                    if num25=='بله':
                        if common_member(evc18,n25)== False :
                            continue
                        else:
                            treffer=treffer+1
                    if num25=='خیر':  
                        if common_member(evc18,n25):
                            treffer=treffer+1
                evc19=e_2.iloc[i]['beleifs']
                if n19=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n19!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num19=='بله':
                        if n19!=evc19:
                            continue
                        if n19==evc19:
                            treffer=treffer+1
                    if num19=='خیر':  
                        if evc19==n19:
                            treffer=treffer+1 
                evc20=e_2.iloc[i]['house_ownership']

                if n22=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n22!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num22=='بله':
                        if evc20=='بله':
                            treffer=treffer+1
                        if evc20=='خیر':       
                             continue
                    if num22=='خیر': 
                         if evc20=='بله':     
                             treffer=treffer+1             
                evc21=e_2.iloc[i]['auto_ownership']

                if n23=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n23!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num23=='بله':
                        if evc21=='بله':
                            treffer=treffer+1
                        if evc21=='خیر':       
                             continue
                    if num23=='خیر': 
                         if evc21=='بله':     
                             treffer=treffer+1   
                evc22=e_2.iloc[i]['employment']

                if n24=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n24!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num24=='بله':
                        if evc22=='بله':
                            treffer=treffer+1
                        if evc22=='خیر':       
                             continue
                    if num24=='خیر': 
                         if evc22=='بله':     
                             treffer=treffer+1   
                evc23=e_2.iloc[i]['marriage_exp']           
                if n20=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n20!='این معیار برای من اهمیت ویژه ای ندارد':

                    if num20=='بله':
                        if n20!=evc23:
                            continue
                        if n20==evc23:
                            treffer=treffer+1
                    if num20=='خیر':  
                        if evc23==n20:
                            treffer=treffer+1  
                evc24=e_2.iloc[i]['want_children']           
                if n21=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n21!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num21=='بله':
                        if n21!=evc24:
                            continue
                        if n21==evc24:
                            treffer=treffer+1
                    if num21=='خیر':  
                        if evc24==n21:
                            treffer=treffer+1             
                evc25=e_2.iloc[i]['family_job'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n6:
                    treffer=treffer+1
                else:  
                    if num6=='بله':
                        if common_member(evc25,n6)==False :
                            continue
                        else:
                            treffer=treffer+1
                    if num6=='خیر':  
                        if evc25 in n6:
                            treffer=treffer+1           
                evc26=e_2.iloc[i]['sport']           
                if n1000=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n1000!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num1000=='بله':
                        if n1000!=evc26:
                            continue
                        if n1000==evc26:
                            treffer=treffer+1
                    if num1000=='خیر':  
                        if evc26==n1000:
                            treffer=treffer+1 
                evc27=e_2.iloc[i]['money']           
                if n1001=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n1001!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num1001=='بله':
                        if n1001!=evc27:
                            continue
                        if n1001==evc27:
                            treffer=treffer+1
                    if num1001=='خیر':  
                        if evc27==n1001:
                            treffer=treffer+1 
                evc28=e_2.iloc[i]['politic']           
                if n1002=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n1002!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num1002=='بله':
                        if n1002!=evc28:
                            continue
                        if n1002==evc28:
                            treffer=treffer+1
                    if num1002=='خیر':  
                        if evc28==n1002:
                            treffer=treffer+1 



                evc29=e_2.iloc[i]['fd']    
                if n1003=='خیلی از آشنایی با او ناامید میشوم':  
                    if evc29=='بله':
                        continue
                    else:
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc30=e_2.iloc[i]['fj']    
                if n1004=='خیلی از آشنایی با او ناامید میشوم':  
                    if evc30=='بله':
                        continue
                    else:
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc31=e_2.iloc[i]['food']    
                if n1005=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc31=='بله':
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc32=e_2.iloc[i]['zaher']    
                if n1006=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc32=='بله':
                        treffer=treffer+1   
                else:
                    treffer=treffer+1
                evc33=e_2.iloc[i]['study']    
                if n1007=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc33=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc34=e_2.iloc[i]['din']    
                if n1008=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc34=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc35=e_2.iloc[i]['moh']    
                if n1009=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc35=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc36=e_2.iloc[i]['humor']    
                if n1010=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc36=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc37=e_2.iloc[i]['mood']
                if n1011=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n1011!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num1011=='بله':
                        if n1011 != evc37:
                            continue
                        else:
                            treffer=treffer+1
                    if num1011=='خیر':  
                        if n1011 == evc37:
                            treffer=treffer+1
                evc38=e_2.iloc[i]['c_il']           
                if n2000=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n2000!='این معیار برای من اهمیت ویژه ای ندارد':

                    if num2000=='بله':
                        if n2000!=evc38:
                            continue
                        if n2000==evc38:
                            treffer=treffer+1
                    if num2000=='خیر':  
                        if evc38==n2000:
                            treffer=treffer+1 
                evc39=e_2.iloc[i]['eg'] 
                if n3000=='خیلی از آشنایی با او ناامید میشوم':  
                    if evc39=='بله':
                        continue
                    else:
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc40=e_2.iloc[i]['family_number']
                if n5000=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n5000!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num5000=='بله':
                        if n5000 != evc40:
                            continue
                        else:
                            treffer=treffer+1
                    if num5000=='خیر':  
                        if n5000 == evc40:
                            treffer=treffer+1
                evc41=e_2.iloc[i]['doa']    
                if n1012=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc41=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc42=e_2.iloc[i]['music']    
                if n1013=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc42=='بله':
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                evc43=e_2.iloc[i]['c_nava']
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n6000:

                    treffer=treffer+1
                else:  
                    if num6000=='بله':
                        if common_member(n6000,evc43)== False :
                            continue
                        else:
                            treffer=treffer+1
                    if num6000=='خیر':  
                        if common_member(n6000,evc43):
                            treffer=treffer+1
                evc44=e_2.iloc[i]['des'] 
                if n7000=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n7000!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num7000=='بله':
                        if evc44=='بله':
                            continue
                        if evc44=='خیر':       
                             treffer=treffer+1
                    if num7000=='خیر': 
                        if evc44=='خیر':       
                             treffer=treffer+1
                evc45=e_2.iloc[i]['vas']    
                if n8000=='خیلی از آشنایی با او ناامید میشوم':  
                    if evc45=='بله':
                        continue
                    else:
                        treffer=treffer+1
                else:
                    treffer=treffer+1
                evc46=e_2.iloc[i]['ramezan'] 
                if n999=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                if n999!='این معیار برای من اهمیت ویژه ای ندارد':
                    if num999=='بله':
                        if evc46!=n999:
                            continue
                        else:       
                             treffer=treffer+1
                    if num999=='خیر': 
                        if evc46==n999:       
                             treffer=treffer+1  
                evc47=e_2.iloc[i]['c_dur']           
                if n222=='این معیار برای من اهمیت ویژه ای ندارد':

                    treffer=treffer+1
                if n222!='این معیار برای من اهمیت ویژه ای ندارد':  
                    if num222=='بله':
                        if n222!=evc47:
                            continue
                        else:
                            treffer=treffer+1
                    if num222=='خیر':  
                        if evc47==n222:
                            treffer=treffer+1
                evc48=e_2.iloc[i]['bakh'] 
                if n213=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                else:
                    if num213=='بله':
                        if n213!=evc48:
                            continue
                        else:
                            treffer=treffer+1
                    if num213=='خیر':
                        if n213==evc48:
                            treffer=treffer+1
                evc49=e_2.iloc[i]['negah'] 
                if n313=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                else:
                    if num313=='بله':
                        if n313!=evc49:
                            continue
                        else:
                            treffer=treffer+1
                    if num313=='خیر':
                        if n313==evc49:
                            treffer=treffer+1
                evc50=e_2.iloc[i]['harf'] 
                if n413=='این معیار برای من اهمیت ویژه ای ندارد':
                    treffer=treffer+1
                else:
                    if num413=='بله':
                        if n413!=evc50:
                            continue
                        else:
                            treffer=treffer+1
                    if num413=='خیر':
                        if n413==evc50:
                            treffer=treffer+1
                evc51=e_2.iloc[i]['hair'] 
                if 'این معیار برای من اهمیت ویژه ای ندارد' in n150:
                    treffer=treffer+1
                else:  
                    if num150=='بله':
                        if evc51 not in n150:
                            continue
                        if evc51 in n150:
                            treffer=treffer+1
                    if num150=='خیر':  
                        if evc51 in n150:
                            treffer=treffer+1
                evc52=e_2.iloc[i]['c_kadu']    
                if n2222=='این معیار برای من اهمیت ویژه ای دارد':  
                    if evc52==n2222:
                        treffer=treffer+1 
                else:
                    treffer=treffer+1
                if treffer/52>=num8765:
                    candidate=[e_2.iloc[i]['id'],treffer/52]
                    basket.append(candidate) #


                    li=eval(e_2.iloc[i]['candidate_list'])
                    #edited_li=[]
                    for j in li:
                        if j[0]== num0:
                            #edited_li.append([j[0],j[1]])
                            hisher_basket.append([j[0],j[1]])
                            my_basket.append(candidate)
                    #hisher_basket.append(edited_li)
                    
                #hisher_basket.append(li)
            
            ex=pd.read_sql("select * from F", getPandasfromtable (1))
            pd.DataFrame(ex)   
            ex.loc[ex['id']==num0, ['candidate_list']] = str(basket)
            ex=ex.applymap(str)

            #ex[col] = ex.astype('string')
            engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**st.secrets["mysql"]))
            
            ex.to_sql(con=engine, name='F', if_exists='replace', index=False)#
            
            
            
            
            
            
            
        




    
    st.write("")
    st.write("")
    #st.dataframe(st.session_state['m_table'])
    st.markdown('<div style="text-align: center;color:Gray">دقت کنید که معرفی گزینه ها در معیار منوط به جستجو شدن طرفین مراجعه کننده توسط هم و مراجعه لزوما بیشتر از یکبار است</div>', unsafe_allow_html=True)
    result = {'شما':num0 , 'دیگران در نگاه شما': my_basket,'شما در نگاه دیگران': hisher_basket}
    re = pd.DataFrame(result)
    re.style.set_properties(**{'background-color': 'white', 'color': 'black', 'border-color': 'white'})
    st.dataframe(re)  
    #st.dataframe(exii)
    #st.dataframe(exi)
#st.success("")
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    


