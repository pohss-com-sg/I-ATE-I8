path = "/static/needed.json"
//jsonfile by chatgpt --> couldnt find what i needed online so we asked gpt to generate one

function jsonfile(path) {
    //with help from Geeks4Geeks schools importing json file to js https://www.geeksforgeeks.org/javascript/javascript-fetch-method/

    //TLDR: THIS IS PROBABLY STUPIDLY INEFFICENT BUT IM NOT VERY PROFICIENT IN JS PLS FORGIVE ME
    //takes the info from json file and transfer it to template with 1. name of food and 2. the contents in the food e.g Pork 100g, 200calories 20gram fat...
    //gives the template its own id for each diff food
    //appends the element id into a list and returns it from the searching variable

    const template = document.querySelector("[data-template]");
    const datacontainer = document.querySelector("[data-container]");

    const foods = [];
    fetch(path)
        //gets the json file and access all data inside and duplicate into template
        .then(response => response.json())
        .then(data => {
            data.forEach(food => {
                const eachdata = template.content.cloneNode(true)
                const button = eachdata.querySelector(".dbbutton")
                const name = eachdata.querySelector("[name-data]")
                const databody = eachdata.querySelector("[nutrient-data]")
                const dropdown_container = eachdata.querySelector(".dropdown-container")
                const arrowdown = eachdata.querySelector(".fa-caret-down")
                const arrowup = eachdata.querySelector(".fa-caret-up")
               
                button.setAttribute("id", `${food.name}`)
                arrowdown.setAttribute("id", `arrow-up-${food.name}`)
                arrowup.setAttribute("id", `arrow-down-${food.name}`)
                dropdown_container.setAttribute("id", `drop-${food.name}`)


                name.textContent = food.name
                databody.textContent = food.body //in json but i need to see if need for loop to contain all the values proeprly

                datacontainer.append(eachdata)
                
                foods.push(document.getElementById(`${food.name}`))

            })
        })
        console.log(foods)
        return foods
}

jsonfile(path)


function dropdown(id) {
    //get by class not using queryselect (i forgot to change this from the func lol)
    //when dropped down check if any other element is dropped down and hides the element
    const dropdown_container = document.getElementsByClassName(".dropdown-container")
    const arrowdown = document.getElementsByClassName(".fa-caret-down")
    const arrowup = document.getElementsByClassName(".fa-caret-up")

    for (let i = 0; i < dropdown_container; i++) {
        if (dropdown_container[i].style.display != "none") {
            dropdown_container[i].style.display = "none" 
            arrowdown[i].style.display = "block"
            arrowup[i].style.display = "none"
            console.log("closed" + `${i}`) //check whether all dropdown is closed
    
        } else {
            continue //if none is open then we continue idt this is neccessary but ill just keep it
        }
    }

    //main part where we get the dropdown to work when clicked

    const dropdown_container2 = document.getElementsByClassName(".dropdown-container")
    const arrowdown2 = document.getElementsByClassName(".fa-caret-down")
    const arrowup2 = document.getElementsByClassName(".fa-caret-up")
    dropdown_container2.style.display = "flex" //set new display for dropdown just make sure theres no interference pls if not must find again
    dropdown_container2.style.flexDirection = "row" 
    arrowdown2.style.display = "block"
    arrowup2.style.display = "none"
    console.log("open" + `${id}`) //check for open can remove later if we want
}

window.onclick = function(event) {
    //if clicked outside any window it will close off all dropped down elements.
    //reuse the previous functions checking method but only when clicked away for judges to understand

    if(!event.target.closest(".card") && !event.target.closest(".dropdown-container")) { //idk why target.matches doesnt work correctly btw (very buggy) so imma just use closest
        const dropdown_container = eachdata.querySelector(".dropdown-container")
        const arrowdown = eachdata.querySelector(".fa-caret-down")
        const arrowup = eachdata.querySelector(".fa-caret-up")

        for (let i = 0; i < dropdown_container; i++) {
            if (dropdown_container[i].style.display != "none") {
                dropdown_container[i].style.display = "none" 
                arrowdown[i].style.display = "none"
                arrowup[i].style.display = "block" //change arrowdown to up to show the dropdown --> see if we can put a slow transition here maybe we can make it look betteter
                console.log("closed" + `${i}`) //check whether all dropdown is closed
        
                } 
            }
        }
}

food_list = jsonfile(path)

const foodlist = food_list

//searchbar work function

search.addEventListener("input", e => { //checks for input in the search bar input in the html file
    const value = e.target.value.toLowerCase(); //lowercase so everything can match with database and not show error
    console.log(value) //check for the words so i can see in console
    foodlist.forEach(food => {
        const show = food.id.toLowerCase().includes(value);
        food.classList.toggle("hide", !show) //check in css file
    })
})





