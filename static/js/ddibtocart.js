const itemcartModals = document.querySelectorAll('.item-cart-modals')
itemcartModals.forEach(modal => {
  const itemId = modal.getAttribute('data-item-id')
  const quantityField = document.querySelector(`#quantity-${itemId}`)
  console.log(quantityField)
  const defaultItemPrice = document.querySelector(`#price-${itemId}`).innerText // 각 상품의 기본 가격 (1개 가격)
  const itemPriceField = document.querySelector(`#price-${itemId}-field`)  // 각 상품 가격 * 수량 표시 필드
  itemPriceField.innerText = defaultItemPrice // 처음 모달창 클릭시 0원이 아닌 상품 기본 가격으로 표시
  // 수량 입력 이벤트
  quantityField.addEventListener('input', event => { 
    itemPriceField.innerText = defaultItemPrice * event.target.value 
  })
})



