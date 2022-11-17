/* 1. 장바구니 수량에 따른 계산 */
const checkBoxes = document.querySelectorAll('.item-checkboxes')
let itemPriceDict = {}  // item-id : price
let totalPrice = 0
const productsPriceField = document.querySelector('#products-price')  // 모든 상품 가격을 합친 금액
const totalPriceField = document.querySelector('#total-price') // = productsPriceField

checkBoxes.forEach(checkBox => {
  const itemId = checkBox.getAttribute('data-item-id')
  const quantityField = document.querySelector(`#quantity-${itemId}`)
  // console.log(`${checkBox.checked} ${itemId}`)
  
  const defaultItemPrice = document.querySelector(`#price-${itemId}`).innerText // 각 상품의 기본 가격 (1개 가격)
  const itemPriceField = document.querySelector(`#price-${itemId}-field`)  // 각 상품 가격 * 수량 표시 필드
  
  itemPriceField.innerText = defaultItemPrice * quantityField.value
  
  // 체크박스 클릭 이벤트
  checkBox.addEventListener('click', event => {
    // 체크됐을 때만 수량 변경 O
    if (checkBox.checked === true) {
      quantityField.disabled = false
      itemPriceField.setAttribute('data-is-disabled', 'false')
      
      if (itemPriceField.getAttribute('data-is-disabled') === 'false') {
        itemPriceField.innerText = defaultItemPrice * quantityField.value
        itemPriceDict[itemId] = Number(itemPriceField.innerText)
        
        let tmp = 0
        for (let key of Object.keys(itemPriceDict)) {
          tmp += itemPriceDict[key]
        }
        totalPrice = tmp
        productsPriceField.innerText = totalPrice + '원'
        totalPriceField.innerText = totalPrice + '원'
      }

      // 수량 입력 이벤트
      quantityField.addEventListener('input', event => {
        // event.stopPropagation() // 버블링 방지
        if (itemPriceField.getAttribute('data-is-disabled') === 'false') {
          itemPriceField.innerText = defaultItemPrice * event.target.value
          itemPriceDict[itemId] = Number(itemPriceField.innerText)
          
          let tmp = 0
          for (let key of Object.keys(itemPriceDict)) {
            tmp += itemPriceDict[key]
          }
          totalPrice = tmp
          productsPriceField.innerText = totalPrice + '원'
          totalPriceField.innerText = totalPrice + '원'
        }
      })
    } else {
      quantityField.disabled = true
      itemPriceField.setAttribute('data-is-disabled', 'true')

      if (itemPriceField.getAttribute('data-is-disabled') === 'true') {
        itemPriceField.innerText = defaultItemPrice * quantityField.value
        // 선택되지 않은 상품의 가격을 0으로
        itemPriceDict[itemId] = 0

        let tmp = 0
        for (let key of Object.keys(itemPriceDict)) {
            tmp += itemPriceDict[key]
        }
        totalPrice = tmp
        productsPriceField.innerText = totalPrice + '원'
        totalPriceField.innerText = totalPrice + '원'
      }
    }
  })
})


/* 2. enter키로 form 제출 방지 */
const cartUpdateForm = document.querySelector('#cart-update-form')
cartUpdateForm.onkeypress = function(event) {
  if (event.keyCode == 13) {
    event.preventDefault()
  }
}


/* 3. 삭제 비동기 */
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
cartUpdateForm.addEventListener('submit', event => {
  event.preventDefault()
  // console.log(event.submitter)

  // view로 넘겨줄 formData 생성
  let formData = new FormData(cartUpdateForm)
  
  // submit input들의 name:value 쌍 저장
  formData.append('kindOfSubmit', event.submitter.name)
  if (event.submitter.name === 'delete') {
    // console.log(event.submitter.value)
    formData.append('productPk', event.submitter.value)
  }

  axios({
    method: 'post',
    url: '/accounts/cart/update/',
    headers: {'X-CSRFToken': csrfToken},
    data: formData,
  })
  .then(response => {
    const deletedItemList = response.data.deletedItemList
    // console.log(deletedItemList)
    
    for (let value of deletedItemList) {
      const productBox = document.querySelector(`#product-${value}-box`)
      productBox.remove()
    }
  })
})


/* 4. 구매 완료하면 장바구니 비우기? */