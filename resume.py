import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np
import time
import requests
from streamlit_extras.streaming_write import write
from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention
from annotated_text import annotated_text
from streamlit_extras.tags import tagger_component
from streamlit_extras.let_it_rain import rain
def stream_gpx(github_url):
    # 获取GitHub文件的内容
    response = requests.get(github_url)
    response.raise_for_status()  
    
    content = response.text
    yield content
    time.sleep(0.1)

# 设置页面配置
st.set_page_config(
    page_title="个人简历|张际",
    page_icon=":wave:",
    layout="wide", 
    initial_sidebar_state="collapsed",
)
with st.sidebar:
    mention(
        label="我的个人博客",
        icon="✨", 
        url="http://ningning.love",
    )
    with st.spinner("Loading..."):
        time.sleep(0.1)
    st.success("欢迎来到我的个人简历!")

# 居中显示内容
left_margin = st.empty()
left_margin.write("")
left_margin = st.sidebar.empty()
left_margin.write("")

# 列布局
col1, col2 = st.columns([3, 1])

# 基本信息
with col1:
    colored_header(
        label="基本信息",
        description="下面由我介绍一下我自己~",
        color_name="violet-70",
    )
    st.write("张际 | 男 | 年龄：22岁 | 本科 | 期望城市：上海/杭州")
    st.markdown('<img src="https://benyuan-house.oss-cn-shanghai.aliyuncs.com/3/%E6%89%8B%E6%9C%BA.png" width="20" height="20"> 17777494009', unsafe_allow_html=True)
    st.markdown('<img src="https://benyuan-house.oss-cn-shanghai.aliyuncs.com/3/%E5%BE%AE%E4%BF%A1.png" width="20" height="20"> navoooo', unsafe_allow_html=True)
    mention(
        label="benyuanya@gmail.com",
        icon="https://benyuan-house.oss-cn-shanghai.aliyuncs.com/3/%E9%82%AE%E7%AE%B1%20%281%29.png", 
        url="benyuanya@gmail.com",
    )
    mention(
        label="https://github.com/benyuan2333",
        icon="github", 
        url="https://github.com/benyuan2333",
    )

# 头像
with col2:
    st.markdown('<img src="https://benyuan-house.oss-cn-shanghai.aliyuncs.com/1/%E6%9C%AC%E4%BA%BA.jpg" alt="Rinyom_zhang" width="150" style="margin-top: 110px;">', unsafe_allow_html=True)


# 教育背景
colored_header(
        label="教育背景",
        description="",
        color_name="blue-70",
    )
st.write("""
- **武汉科技大学城市学院 - 本科 - 计算机科学与技术**  
  2020.09 - 2024.06  
  专业排名：前10%  
  成绩优异，21年获得 中国大学生计算机设计大赛 省二等奖  
  曾任校IOS Club Swift编程部部长，多次协助导师演讲  
- **英山一中 - 理科**  
  2017.09 - 2020.06  
  积极参与课外竞赛，热爱拼搏  
""")

# 工作经验
colored_header(
        label="工作经验",
        description="",
        color_name="orange-70",
    )
st.write("""
- **奇点临近技术（上海）有限公司 - 软件实习**  
  2023年12月 - 现在  
  对公司生产的AR智能眼镜进行软硬件测试，使用Python编写自动化测试脚本。  
  骑行App运动路书开发，收集并清洗标注对接mysql数据库。  
  高尔夫App球场数据开发，gis绘制Shp，转换geojson以及开发所需json格式。  
  三方应用测试，三方应用商店部署，Api-demo与微信硬件小程序框架开发。  
  各类爬虫脚本攥写与清洗可视化。  
""")

# 技能
colored_header(
        label="技能",
        description="",
        color_name="red-70",
    )
skills = ["Python", "Java", "C/C++", "Vue", "H5", "Sprintboot", "JavaScript", "MySQL", "Git", "Docker", "Kubernetes"]
proficiency = [90, 80, 70, 80, 90, 90, 85, 90, 75, 90, 60]

selected_skill = st.selectbox('选择技能', skills)
index = skills.index(selected_skill)
st.text("熟练度")
st.progress(proficiency[index] / 100)
st.write("""
 **个人优势**  
  具备良好的问题解决能力，团队合作能力，热爱交流，学习能力强。
  具有良好的创新思维和专业知识，热爱钻研技术，相关技术栈。  
- 熟悉主流编程语言，包括C/C++、Java和Python。  
- 掌握前端技术，包括HTML、CSS、JavaScript，以及Vue2和Element等框架。  
- 灵活运用开发框架，Sprintboot,Django等。
- 具备Mysql、Redis数据经库设计管理能力，熟悉Sql语言。  
- 熟练使用各类开发工具,如VScode,Idea等。
- 掌握Qgis、ArcGis、Cad等绘制工具。
- Linux云服务器精通使用，熟悉常见命令，Docker和Kubernetes的应用。
- 拥有网络运维技术，能解决大多数网络运维问题，熟悉软硬路由固件编译和使用
- 深度了解固件烧录，Adb调试命令，能够适应大部分开发测试。
""")
# 项目
colored_header(
        label="项目",
        description="",
        color_name="blue-70",
    )
st.subheader("基于SSM的房屋出租管理系统")
tagger_component("涉及技术：", ["Java", "Sprint", "MyBatisPlus", "Bootstrap", "Thymeleaf", "Druid"], color_name=["blue", "orange", "lightblue", "lightpink", "red", "green"])
st.write("**责任:** 负责前后端开发，使用SSM框架。")
col3, col4 = st.columns(2)
with col3:
    st.write("""
    **前端:** 
    - 使用Bootstrap作为前端开发框架
    - 使用JavaScript、JQuery实现动态功能，增强浏览效果
    - 使用HTML、CSS设计网页内容和样式  
    """)

with col4:
    st.write("""
    **后端:** 
    - 使用Spring、Spring MVC和MyBatisPlus构建后端
    - 集成Thymeleaf模板引擎和Druid数据库连接池
    - 使用MySQL数据库进行数据存储
    - 架构以分层模式构建，主要分为表示层（用户界面）、业务逻辑层（服务层）、持久层（数据访问层）以及数据库层
    """)
st.subheader("小额贷款平台后台管理系统")
tagger_component("涉及技术：", ["Vue", "Java", "Sprintboot", "Mysql", "Mybatis", "ElementUI"], color_name=["blue", "orange", "lightblue", "lightpink", "red", "green"])
st.write("**责任:** 负责前端开发，使用Vue2组件化开发，参与设计和开发后台管理系统的核心功能模块。")
col5, col6 = st.columns(2)
with col5:
    st.write("""
    **前端:** 
    - 使用Element UI作为前端UI框架，提高开发效率
    - 使用Vue各类组件构建页面主题框架
    - Methods&Style设计以及攥写 
    """)

with col6:
    st.write("""
    **后端:** 
    - 使用MyBatis简化与Mysql数据库交互
    - 使用Springboot框架构建后端
    - 使用RESTful API接口设计，确保前后端数据交互的可靠性
    """)
st.subheader("Python爬虫&可视化")
tagger_component("涉及技术：", ["Python", "Ttkbootstrap", "Hmac", "Pandas", "ProxyPool", "多线程"], color_name=["blue", "orange", "lightblue", "lightpink", "red", "green"])
st.write("**责任:** 负责对需求内容爬取并清洗，攥写可视化程序，Hmac解密验证Api请求")
col5, col6 = st.columns(2)
with col5:
    st.write("""
    **爬虫:** 
    - 使用Python编写爬虫程序，通过分析网页和API接口的源码实现数据抓取
    - 利用多线程提升爬取效率，结合代理池处理IP封锁问题
    - 数据清洗与预处理，确保数据质量和可用性
    """)

with col6:
    st.write("""
    **可视化:** 
    - 使用Ttkbootstrap和其他可视化工具库设计和开发用户界面
    - 使用Pandas进行数据分析和处理，生成可视化报表和图表
    - 实现HMAC解密验证API请求的功能，确保数据安全和完整性
    """)

# 设定按钮的初始状态
if 'show_code' not in st.session_state:
    st.session_state.show_code = False

# 按钮点击事件
if st.button("路书相关爬虫代码展示"):
    st.session_state.show_code = not st.session_state.show_code

# 显示或隐藏代码块
if st.session_state.show_code:
    github_url = 'https://raw.githubusercontent.com/benyuan2333/loan_platform/main/GetGpxGuiNew.py'
    for block in stream_gpx(github_url):
        st.code(block)  

# 其他信息
colored_header(
        label="其他信息",
        description="",
        color_name="green-70",
    )
st.write("**爱好:** 骑行，旅游，美食以及撸猫~ ")

# 联系方式
colored_header(
        label="联系方式",
        description="",
        color_name="red-60",
    )
annotated_text("如果您对我的简历感兴趣，请通过", ("邮箱", "benyuanya@gmail.com", "#bff"),"&",("微信", "navoooo", "#afa"), "联系我。")

# 简历下载
colored_header(
        label="简历下载",
        description="",
        color_name="orange-60",
    )

def download_pdf(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content

resume_url = 'https://raw.githubusercontent.com/benyuan2333/Streamlit_resume/main/resume.pdf'

st.download_button(
    label="下载简历",
    data=download_pdf(resume_url),
    file_name="简历.pdf",
    mime="application/pdf",
)
def snow():
    rain(
        emoji="✨",
        font_size=20,
        falling_speed=5,
        animation_length=1,
    )
snow()
