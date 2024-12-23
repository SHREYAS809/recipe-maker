import React, { useState, useEffect } from 'react';

function App() {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/recipes')
      .then(response => response.json())
      .then(data => setRecipes(data))
      .catch(error => console.error('Error fetching recipes:', error));
  }, []);

  return (
    <div>
      <h1>Recipe Maker</h1>
      <ul>
        {recipes.map(recipe => (
          <li key={recipe.id}>
            <strong>{recipe.name}</strong>: {recipe.ingredients.join(', ')}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
