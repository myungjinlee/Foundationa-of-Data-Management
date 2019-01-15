select title, name as category 
from film, film_category, category 
where film.film_id=film_category.film_id 
and film_category.category_id=category.category_id 
order by title;
