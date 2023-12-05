document.addEventListener("DOMContentLoaded", function() {
    var box = document.querySelectorAll(".items_menu"); 

    box.forEach(function(item) {
        item.addEventListener('mouseover', function() {
            item.style.color = 'red';
        });
        item.addEventListener('mouseout', function() {
            item.style.color = '';
        });
    });
});


