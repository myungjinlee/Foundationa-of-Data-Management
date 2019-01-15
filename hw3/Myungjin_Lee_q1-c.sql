select name as category, count(*) as number_of_films 
from film, film_category, category 
where film.film_id=film_category.film_id 
and film_category.category_id=category.category_id 
group by category 
having number_of_films>=60 
order by number_of_films desc;
