---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

# sections:
#   - block: hero
#     content:
#       title:
# date: 2022-10-24
# type: landing

sections:
  # - block: about.biography
  #   id: content.authors.admin.biography
  #   content:
  #     title: Biography
  - block: hero
    content:
      title: |
        <span style="color:#fff;font-size:2.6rem;font-weight:bold;letter-spacing:2px;">GrokCV Group</span>
      text: |
        <span style="color:#fff;font-size:1.05rem;">
        长期致力于红外弱小目标检测与遥感多模态视觉感知
        </span>
    design:
      text_align: center
      text_color_light: true
      background:
        image:
          filename: bg7.jpg
          size: cover
          position: center
          overlay_color: "#003366"
          overlay_opacity: 0.5
          parallax: false
      

  #     text: |
  #       <br>
        
  #       The **GrokCV Group** has been a center of excellence for Artificial Intelligence research, teaching, and practice since its founding in 2016.
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen
---
