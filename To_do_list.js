const todoList=[{
    name:'dinner',
    duedate:'2022-12-22'
},{
    name:'netflix',
    duedate:'2022-12-12'
}];

functiontodoList();

function functiontodoList(){
let todoListHTML='';

todoList.forEach((todoObject,index) => {
    //const name=todoObject.name;
    //const duedate=todoObject.duedate;
    const {name}=todoObject;
    const {duedate} = todoObject;
    const html=`
        <div>${name}</div>
        <div>${duedate}</div>
        <button class="delete-todo-button js-delete-todo-button">Delete</button>`
    
    todoListHTML+=html;
});
/*for(let i=0;i< todoList.length;i++){
    const todoObject =todoList[i];
    //const name=todoObject.name;
    //const duedate=todoObject.duedate;
    const {name}=todoObject;
    const {duedate} = todoObject;
    const html=`
        <div>${name}</div>
        <div>${duedate}</div>
        <button onclick="
            todoList.splice(${i},1);
            functiontodoList();
        "class="delete-todo-button">Delete</button>`
    
    todoListHTML+=html;
}*/

document.querySelector('.js-todo-list')
.innerHTML=todoListHTML;

document.querySelectorAll('.js-delete-todo-button')
    .forEach((deleteButton,index) => {
        deleteButton.addEventListener('click', () =>{
            todoList.splice(index,1);
            functiontodoList();
        })
    })

}

document.querySelector('.js-add-todo-button').addEventListener('click',() =>{
    addTodo();
})
function addTodo(){
    const inputElement=document.querySelector('.js-name-input');
    const name = inputElement.value;
    const dateInputElement=document.querySelector('.js-due-date');
    const duedate =dateInputElement.value;

    todoList.push({name,duedate});
    console.log(todoList);

    inputElement.value='';
    functiontodoList();

}