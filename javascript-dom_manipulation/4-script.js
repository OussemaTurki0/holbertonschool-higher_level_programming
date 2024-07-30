let addItem = document.getElementById('add_item');
addItem.addEventListener('click',function (){
    let item = document.createElement('li');
    item.textContent='item';

    let mylist= document.querySelector('.my_list')
    mylist.appendChild(item)
})
