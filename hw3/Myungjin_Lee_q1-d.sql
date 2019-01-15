select name as category_name 
from film, film_category, category 
where film.film_id=film_category.film_id 
and film_category.category_id=category.category_id 
group by category_name 
having count(*) >= all(select count(*) from film, film_category, category where film.film_id=film_category.film_id and film_category.category_id=category.category_id group by category.name);

