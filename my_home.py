'''我的主页'''
import streamlit as st
import time
from PIL import Image

page = st.sidebar.radio("我的主页", ["视频软件网页", "音乐软件网页", "图片处理器", "词典", "我的留言区", "世界地图"])

def page_1():
    "视频软件网页"
    st.write(":sunglasses:视频软件网页:sunglasses")
    tab1,tab2,tab3,tab4 = st.tabs(['哔哩哔哩','腾讯视频','爱奇艺','芒果TV'])
    with tab1:
        st.link_button("哔哩哔哩首页", "https://www.bilibili.com/")
    with tab2:
        st.link_button("腾讯视频首页", "https://v.qq.com/")
    with tab3:
        st.link_button("爱奇艺首页", "https://www.iqiyi.com/?vfm=f_588_wrb&fv=ac30238882b84c8c")
    with tab4:
        st.link_button("芒果TV首页", "https://www.mgtv.com/?cxid=bfan6mqcg")

def page_2():
    "音乐软件网页"
    st.write(":sunglasses:音乐软件网页:sunglasses")
    with open('The Rah Band - Messages from the Stars (Sped Up).mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    tab1,tab2,tab3, = st.tabs(['酷狗音乐','网易云音乐','QQ音乐'])
    with tab1:
        st.link_button("酷狗音乐首页", "https://www.kugou.com/")
    with tab2:
        st.link_button("网易云音乐首页", "https://music.163.com/")
    with tab3:
        st.link_button("QQ音乐首页", "https://y.qq.com/")

def page_3():
    "图片处理器"
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))

def img_change(img, rc, gc, bc):
    '''图片处理器'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

def page_4():
    '''词典'''
    st.write('词典'[1])
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
     # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
    if word == 'python':
            st.code('''
                # 恭喜你触发彩蛋，这是一行python代码
                print('hello world')''')
    if word == 'snow':
        st.snow()
    if word == 'birthday':
        st.balloons()

def page_5():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_6():
    data = {
        'latitude': [37.7749, 34.0522, 40.7128],
        'longitude': [-122.4194, -118.2437, -74.0060],
        'name': ['San Francisco', 'Los Angeles', 'New York']
    }
     
    st.map(data, zoom=4, use_container_width=True)

if page == "视频软件网页":
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
    page_1()
elif page == "音乐软件网页":
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
    page_2()
elif page == "图片处理器":
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
    page_3()
elif page == "词典":
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
    page_4()
elif page == "我的留言区":
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
    page_5()
elif page == "世界地图":
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
    page_6()