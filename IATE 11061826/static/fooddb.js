path = "C:\Users\neozo\OneDrive\Desktop\IATE\needed.json"

function jsonfile(path) {
    //TLDR: THIS IS PROBABLY STUPIDLY INEFFICENT BUT IM NOT VERY PROFICIENT IN JS PLS FORGIVE ME
    //takes the info from json file and transfer it to template with 1. name of food and 2. the contents in the food e.g Pork 100g, 200calories 20gram fat...
    //gives the template its own id for each diff food
    //appends the element id into a list and returns it from the searching variable

    const template = document.querySelector(["data-template"])
    const datacontainer = document.querySelector(["data-container"])

    const foods = [];
    fetch(path)
        //gets the json file and access all data inside and duplicate into template
        .then(response => response.json())
        .then(data => {
            data.forEach(food => {
                const eachdata = template.content.cloneNode(true)
                const name = eachdata.querySelector(["name-data"])
                const button = eachdata.querySelector(".element")
                const databody = eachdata.querySelector(["nutrient-data"])
                const dropdown_container = eachdata.querySelector(".dropdown-container")
                const arrowdown = eachdata.querySelector(".fa-caret-down")
                const arrowup = eachdata.querySelector(".fa-caret-up")
               
                
                arrowdown.setAttribute("id", `arrow-up-${food.name}`)
                arrowup.setAttribute("id", `arrow-down-${food.name}`)
                dropdown_container.setAttribute("id", `drop-${food.name}`)

                name.textContent = food.name
                databody.textContent = food.body //in json but i need to see if need for loop to contain all the values proeprly

                datacontainer.append(eachdata)
                
                foods.push(document.getElementById(`${food.name}`))

            } )
        })
        console.log(foods)
        return foods
}

jsonfile(path)

function dropdown(id) {
    //when dropped down check if any other element is dropped down and hides the element
    //then shows the element clicked

}

window.onclick = function(event) {
    //if clicked outside any window it will close off all dropped down elements.
}



