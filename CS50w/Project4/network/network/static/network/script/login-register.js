document.addEventListener('DOMContentLoaded', () => {

    // * add event to the cross button for removing the alert
    document.querySelector('#remove-alert').addEventListener('click', function(){

        const alertContainer = document.querySelector('#remove-alert').parentElement;

        alertContainer.style.animationPlayState = "running";
        alertContainer.addEventListener('animationend', function(){
            alertContainer.remove()
        });
    });

});