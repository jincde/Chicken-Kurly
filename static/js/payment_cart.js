// 1. 결제 준비
IMP.init("imp74723253") // 가맹점 식별코드


// 2. totalPrice와 checkboxes는 cart.js에 이미 선언되어 있음.
// const totalPrice = document.querySelector('#total-price').innerText
// const checkBoxes = document.querySelectorAll('.item-checkboxes')


// 3. 선택된 상품의 이름만 배열에 담기
let productNameArray = []

checkBoxes.forEach(checkBox => {
  const itemId = checkBox.getAttribute('data-item-id')

  checkBox.addEventListener('click', event => {
    const productName = document.querySelector(`#product-name-${itemId}`).innerText
    if (checkBox.checked === true) {
      productNameArray.push(productName)
    } else {
      const idx = productNameArray.indexOf(productName)
      if (idx > -1) {
        productNameArray.splice(idx, 1)
      }
    }
    
    // 결제 금액이 0원이면 결제 버튼 비활성화
    const btnPayment = document.querySelector('#btn-payment')
    if (totalPrice === '0' || totalPrice === 0) {
      btnPayment.disabled = true
    } else {
      btnPayment.disabled = false
    }
  })
})


// 4. 카카오페이 결제창 띄우기
function requestPay() {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value  
  const cartUpdateForm = document.querySelector('#cart-update-form')
  
  const request_name = (productNameArray.length > 1) ? `${productNameArray[0]} 외 ${productNameArray.length - 1}개` : `${productNameArray[0]}`
  let formData = new FormData(cartUpdateForm)

  IMP.request_pay({ // param
    pg: "kakaopay", // 카카오페이 결제창 호출
    pay_method: "card",
    merchant_uid: 'merchant_' + new Date().getTime(),
    name: request_name,
    amount: Number(totalPrice),
  }, function (rsp) { // callback
    if (rsp.success) {
      formData.append('imp_uid', rsp.imp_uid)
      formData.append('merchant_uid', rsp.merchant_uid)
      
      axios({
        method: 'post',
        url: '/accounts/cart/payment/',
        headers: {'X-CSRFToken': csrfToken},
        data: formData
      })
      .then(response => {
        const productBoxes = document.querySelectorAll('.product-boxes')
        productBoxes.forEach(productBox => {
          productBox.remove()
        })
      })
    } else {
      // 결제 실패 시 로직,
      console.log("결제에 실패하였습니다. 에러 내용: " +  rsp.error_msg);
    }
  });
}