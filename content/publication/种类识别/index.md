---
title: "基于蜂群优化多核支持向量机的淡水鱼种类识别"
authors:
- admin
- 吴一全
- 殷骏
- 戴一冕
- 袁永明

author_notes:
- 
-
- 
-

date: "2014-01-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2014-01-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "农业工程学报"
publication_short: ""

abstract: 为了准确地进行淡水鱼种类自动识别,利用计算机视觉技术,提出了一种基于 Krawtchouk 矩,灰度共生矩阵,蜂群优化多核最小二乘支持向量机(least squares support vector machine,LS-SVM)的识别方法.首先获取淡水鱼样本的灰度图像,计算淡水鱼鱼体的长宽比,鱼头鱼尾的 Krawtchouk 矩不变量形状特征,求得鱼身的灰度共生矩阵纹理特征,将上述形状与纹理特征组合成高维特征向量,并输入到多核LS-SVM,通过人工蜂群(artificial bee colony,ABC)算法对多核LS-SVM中的待定参数进行寻优,ABC算法中的适应度函数为测试样本的识别精度;最后输出识别精度达到最高时的最优参数.利用该方法对鳊鱼,鳙鱼,鲫鱼,草鱼,青鱼5种淡水鱼进行了分类识别,对鳊鱼,鳙鱼,鲫鱼,草鱼4种鱼识别时,各类鱼的识别精度均达到95.83%以上,对鳊鱼,鳙鱼,鲫鱼,青鱼4种鱼识别时,各类鱼的识别精度均达到91.67%以上,对鳊鱼,鳙鱼,鲫鱼,草鱼和青鱼5种鱼识别时,各类鱼的识别精度均达到83.33%以上;与近年来提出的淡水鱼识别方法,BP(back propagation)神经网络方法,单核LS-SVM方法相比,该方法的识别精度更高,从而可快速准确地识别淡水鱼的种类,提高水产养殖的自动化水平.
# Summary. An optional shortened abstract.
summary: 

tags:
- 种类识别
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://scholar.google.com/scholar?cluster=427653277958925073&hl=en&oi=scholarr


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
