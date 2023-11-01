// Using jQuery for simplicity
$(".profile-card").click(function() {
    // Show message form or perform other actions
});

// JavaScript
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.profile-card').forEach(card => {
        card.addEventListener('click', function() {
            const name = this.getAttribute('data-name');
            window.location.href = `/profile/${name}/`; // DjangoのURLルーティングに合わせて調整
        });
    });
});
