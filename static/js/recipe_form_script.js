function createMaterialInputField(){
    var material_input_area = document.getElementById('material_input_area')
    var li = document.createElement('li')
    li.classList = 'w-100 d-felx list-group-item mb-1 mx-auto bg-dark border-secondary '
    li.innerHTML = `
            <input type="text" name="material_name" placeholder="material">
            <input type="number" name="material_quantity" placeholder="quantity">
            <input type="number" name="material_calorie" placeholder="calorie">
    `;
    material_input_area.appendChild(li);
}