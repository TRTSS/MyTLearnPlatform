function GetToastInstance(title, body) {
    let id = 'toast-notify-' + String(document.querySelectorAll('.toast').length);
    let toast = document.createElement('div');
    toast.classList.add('toast');
    toast.classList.add('show');
    toast.id = id;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    toast.innerHTML = `<div class="toast-header">
                <strong class="me-auto">${title}</strong>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
                ${body}
            </div>`;
    return toast;
}

function ShowToast(title, body) {
    let t = GetToastInstance(title, body);
    let holder = document.querySelector('.toast-container');
    holder.append(t);
}