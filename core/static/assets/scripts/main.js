'use strict';

document.addEventListener('DOMContentLoaded', () => {
    const menuItems = $('[data-submenu]');
    const pathKey = window.location.pathname.split('/')[1];

    menuItems.each((key, item) => {  
        // Check whether or not to leave the link active
        if (pathKey === $(item).attr('data-menu')) {
            $(item).addClass('menu-active');

            if ($(item).attr('data-submenu') == 'false') {
                $(item).attr('data-submenu', true);
            }
        }

        if ($(item).attr('data-submenu') === 'true') {
            $(item).find('.submenu').removeClass('h-[0px]');
            $(item).find('.submenu').addClass('h-auto');
        } else if($(item).attr('data-submenu') === 'false') {
            $(item).find('.submenu').removeClass('h-auto');
            $(item).find('.submenu').addClass('h-[0px]');
        }

        $(item).on('click', (event) => {
            // Execute script only if the clicked item is not a link to another page
            if (event.target.href == 'javascript:void(0)') {
                if ($(item).attr('data-submenu') === 'true') {
                    $(item).attr('data-submenu', false);
    
                    if (pathKey !== $(item).attr('data-menu')) {
                        $(item).removeClass('menu-active');
                    }
    
                    setTimeout(() => {
                        $(item).find('.submenu').removeClass('h-auto');
                        $(item).find('.submenu').addClass('h-[0px]');
                    }, 200);
                } else if($(item).attr('data-submenu') === 'false') {
                    $(item).find('.submenu').removeClass('h-[0px]');
                    $(item).find('.submenu').addClass('h-auto');
                    $(item).addClass('menu-active');
    
                    $(item).attr('data-submenu', true);
                }
            }
        });
    });
});

// Select input group
$('[data-select="all"]').on('click', (event) => {
    $(event.target).parent().parent().find('[type="checkbox"]').each((key, item) => {
        item.checked = event.target.checked;
    });
});

// Init Modal Class
Modal.init();

// Prvious page
PageBack.init();