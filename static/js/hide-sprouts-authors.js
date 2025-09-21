// 只在 sprouts（新芽）页面隐藏作者卡片的 JavaScript 解决方案
(function() {
    'use strict';
    
    // 检测当前页面是否为 sprouts 页面
    function isSproutsPage() {
        // 检查 URL 路径
        const path = window.location.pathname;
        return path.includes('/sprouts/') || path.startsWith('/sprouts');
    }
    
    // 隐藏作者卡片的函数
    function hideAuthorCards() {
        if (isSproutsPage()) {
            // 添加 CSS 类来触发隐藏样式
            document.body.classList.add('hide-sprouts-authors');
            
            // 为了确保兼容性，也可以直接设置样式
            const authorElements = document.querySelectorAll(`
                .article-metadata .author-notes,
                .article-metadata .article-authors,
                .page-body .author-card,
                .author-profile,
                .article-container .author-notes,
                .article-container .article-authors,
                .pub-authors,
                .author-profile-card,
                .wg-author,
                [data-widget-id="author"],
                .section-author,
                [class*="author-profile"],
                [class*="author-card"],
                [class*="author-bio"],
                .page-footer .author-card,
                .article-footer .author-card,
                .post-footer .author-card,
                .page-content .author-profile,
                .article-content .author-profile,
                .content .author-profile,
                section[id*="author"],
                .blox-author,
                .widget-author
            `);
            
            authorElements.forEach(element => {
                element.style.display = 'none';
            });
        }
    }
    
    // 页面加载完成后执行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', hideAuthorCards);
    } else {
        hideAuthorCards();
    }
    
    // 为了防止动态加载的内容，使用 MutationObserver
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                hideAuthorCards();
            }
        });
    });
    
    // 观察文档变化
    observer.observe(document.body, { childList: true, subtree: true });
})(); 