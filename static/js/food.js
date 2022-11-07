// function foodsOptions(data) {
//     console.log(data)
//     return `
// <div class="card mx-auto mb-3" id=${data["id"]} style="width: 18rem;">
// <img class="card-img-top" src="/media/${data['image']}" alt="Card image cap">
// <div class="card-body">
// <p class="card-title">${data["name"]}</p>
// <p class="card-text"><b>${data["price"]}</b></p>
// <p class="card-text"><b>${data["description"]}</b></p>
// </div>

// <div class="card-footer p-0 no-gutters">

// {% if food|is_in_cart:request.session.cart %}
// <div class="row no-gutters">
// <form action="/restaurant-index/#${data["id"]}" class="col-2 " method="post">
// {% csrf_token %}
// <input hidden type="text" name='food' value='${data["id"]}'>
// <input hidden type="text" name='remove' value='True'>
// <input type="submit" value=" - " class="btn btn-block btn-light border-right">
// </form>
// <div class="text-center col">{{food|cart_quantity:request.session.cart}} in Cart
// </div>
// <form action="/restaurant-index/#{{food.id}}" class="col-2 " method="post">
// {% csrf_token %}
// <input hidden type="text" name='food' value='{{food.id}}'>
// <input type="submit" value=" + " class="btn btn-block btn-light border-left">
// </form>
// </div>
// {% else %}
// <form action="/restaurant-index/#{{food.id}}" method="POST" class="btn-block">
// {% csrf_token %}
// <input hidden type="text" name='food' value='{{food.id}}'>
// <input type="submit" class="float-right btn btn-light  form-control"
// value="Add To Cart">
// </form>
// {% endif %}
// </div>
// </div>
// </div>

//     `;
// }


// function getSelectedFoodCategory() {
//     var foodCategoryId = $("#food_category").find(":selected").val();
//     $.ajax({
//         url: food_category_url,
//         type: "GET",
//         data: {
//             'food_category': foodCategoryId
//         },
//         success: function (response) {
//             data = response['foods']
//             document.getElementById("foods_id").innerHTML = `${data.map(foodsOptions).join("")}`;
//         }
//     })
// }

// function foodCategoryOptions(data) {
//     return `<option value=${data["id"]}>${data["name"]}</option>`;
// }

// $('#restaurant').change(function () {
//     var restaurantId = $(this).val();
//     $.ajax({
//         url: restaurant_url,
//         type: "GET",
//         data: {
//             'restaurant': restaurantId
//         },
//         success: function (response) {
//             console.log('response: ', response)
//             data = response['food_category']
//             if (data.length > 0) {
//                 document.getElementById("food_category").innerHTML = `
//                 ${data.map(foodCategoryOptions).join("")}`;
//             } else {
//                 document.getElementById("food_category").innerHTML = `<option value>No Record Found</option>`;
//             }
//         }
//     })
// });  

function restaurant_field() {
    restaurant_id = document.getElementById('restaurant').value;
    console.log(restaurant_id)
    window.location = "/restaurant-index/?restaurant=" + restaurant_id;
    console.log(window.location)
}

function food_category_field() {
    food_category_id = document.getElementById('food_category').value;
    console.log(food_category_id)
    window.location = "/restaurant-index/?restaurant=" + restaurant + "&food_category=" + food_category_id;
}