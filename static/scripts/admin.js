const actionButtons = document.querySelectorAll(".action-button");
const tabs = document.querySelectorAll(".tab");

actionButtons.forEach(actionButton => {
    actionButton.addEventListener('click', () => {
        tabs.forEach(tabContent => {
            tabContent.classList.remove('tab-active');
        })
    
        actionButtons.forEach(tab => {
            tab.classList.remove('active');
        })

        const target = document.querySelector(actionButton.dataset.tabTarget)
        target.classList.add('tab-active');
        actionButton.classList.add('active');
    })
})