// blog/static/js/blog.js

window.onload = function() {
    var authorLinks = document.getElementsByClassName('author-link');

    for (let i = 0; i < authorLinks.length; i++) {
        authorLinks[i].addEventListener('click', function(e) {
            if('{{ user.is_authenticated }}' === 'False') {
                e.preventDefault();
                var myModal = new bootstrap.Modal(document.getElementById('myModal'));
                myModal.show();
            }
        });
    }
}
