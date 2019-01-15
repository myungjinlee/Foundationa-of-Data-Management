select count(distinct customer_list.ID) as number_of_customer 
from customer_list, inventory, rental, film, film_category, category 
where customer_list.ID=rental.customer_id 
and rental.inventory_id=inventory.inventory_id 
and inventory.film_id=film.film_id 
and film.film_id=film_category.film_id 
and film_category.category_id=category.category_id 
and category.name="action" 
and customer_list.ID
not in
(select customer_list.ID 
from customer_list, inventory, rental, film, film_category, category 
where customer_list.ID=rental.customer_id 
and rental.inventory_id=inventory.inventory_id 
and inventory.film_id=film.film_id 
and film.film_id=film_category.film_id 
and film_category.category_id=category.category_id 
and category.name="horror");

