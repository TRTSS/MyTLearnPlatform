let activators = document.querySelectorAll('[activate-section]');
activators.forEach(a => {
    a.onclick = function() {
        ShowInfoSection(a.getAttribute('activate-section'));
    }
});

function ShowInfoSection(id) {
    let allSection = document.querySelectorAll('.group-info-section');
    allSection.forEach(section => {
        section.classList.remove('show');
    });
    let sectionToShow = document.querySelector(`#${id}`);
    sectionToShow.classList.add('show');
}