function jsonfile(path) {
    const template = document.querySelector(["data-template"])
    const datacontainer = document.querySelector(["data-container"])

    const food = [];
    fetch(path)
        .then(response => response.json())
        .then(data => {
            data.forEach(food => {
                const eachdata = template.content.cloneNode(true)
                const name = eachdata.querySelector(["name-data"])
                const databody = eachdata.querySelector(["nutrient-data"])
                const dropdown_container = eachdata.querySelector(".dropdown-container")
                const arrowdown = eachdata.querySelector(".fa-caret-down")
                const arrowup = eachdata.querySelector(".fa-caret-up")

                arrowdown.setAttribute("id", `arrow-up-${food.name}`)
                arrowup.setAttribute("id", `arrow-down-${food.name}`)
                dropdown_container.setAttribute("id", `drop-${food.name}`)
                
                console.log(food.calories)

            } )
        })
}

jsonfile("needed.json")

function dropdown(id) {
    
}