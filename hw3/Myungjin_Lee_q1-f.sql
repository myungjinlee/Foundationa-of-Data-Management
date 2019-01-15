select count(distinct customer_list.ID) as num_of_customer_rent_action 
from customer_list, rental, inventory, film, film_category, category 
where customer_list.notes="active" 
and customer_list.ID=rental.customer_id 
and rental.inventory_id=inventory.inventory_id 
and inventory.film_id=film.film_id 
and film.film_id=film_category.film_id 
and film_category.category_id=category.category_id 
and category.name="Action";

