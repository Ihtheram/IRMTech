var updateBtns = document.getElementsByClassName('update-cart')


for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var techId = this.dataset.tech
        var action = this.dataset.action
        console.log('techId:', techId, 'action:', action)

        console.log('USER:', user)

        if (user == 'AnonymousUser') {
            console.log('User not logged in')
        } else {
            updateUserOrder(techId, action)
        }
    })
}


function updateUserOrder(techId, action) {
    console.log('User logged in, sending data')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'techId': techId, 'action': action })
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        location.reload()
    })
}