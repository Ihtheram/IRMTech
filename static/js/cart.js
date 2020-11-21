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



// PROCESSING CHECKOUT FORM DATA
function submitFormData(form, storeurl) {
    console.log('Payment button clicked')
    var userFormData = {
         'name':null,
         'email':null,
         'total':total
    }
    var shippingInfo = {
         'address':null,
         'city':null,
         'state':null,
         'zipcode':null
    }
    
    // TAKE USER ADDRESS FROM FORM VALUES FOR PHYSICAL TECHS
    if(shipping != 'False') {
         shippingInfo.address = form.address.value
         shippingInfo.city = form.city.value
         shippingInfo.state = form.state.value
         shippingInfo.zipcode = form.zipcode.value
    }

    // TAKE USER INFO FROM FORM VALUES FOR GUEST USER
    if(user == 'AnonymousUser') {
         userFormData.name = form.name.value
         userFormData.email = form.email.value
    }


    console.log('Shipping Info:', shippingInfo)
    console.log('User Info:', userFormData)

    var url = '/process_order/'
    fetch(url,{
         method:'POST',
         headers:{
              'Content-Type':'application/json',
              'X-CSRFToken': csrftoken
         },
         body:JSON.stringify({'form':userFormData, 'shipping':shippingInfo})
    })
    .then((response) => response.json())
    .then((data) => {
         console.log('Success:', data);
         alert('Transaction completed');
         window.location.href = storeurl
    })
}