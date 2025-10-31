import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [searched, setSearched] = useState(false);
  const [results, setResults] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();
    const apiUrl = `http://localhost:8000/api/leyes/?search=${encodeURIComponent(query)}`;
    const response = await fetch(apiUrl);
    const data = await response.json();
    const filtered = data.results || [];
    console.log(filtered)
    setResults(filtered);
    setSearched(true);
  };

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "0 auto" }}>
      <h1>Buscador de Leyes</h1>

      <form style={{ marginBottom: "20px" }} onSubmit={handleSearch}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Escribe tu búsqueda..."
          style={{ padding: "8px", width: "70%", marginRight: "10px" }}
        />
        <button type="submit" style={{ padding: "8px 16px" }}>
          Buscar
        </button>
      </form>

      <div>
        {results.length > 0 ? (
          <ul>
            {results.map((ley) => (
              <li key={ley.id}>
                <p>{ley.titulo}</p>
                <a target="_blank" style={{ color: "white", textDecoration: "underline" }} href={ley.historial.sort((a, b) => new Date(a.fecha_ppo) - new Date(b.fecha_ppo)).reverse()[0].rutaArchivo}>Ver Documento</a>
              </li>
            ))}
          </ul>
        ) : (
          searched && <p>No se encontraron resultados</p>
        )}
      </div>
    </div>
  );
}
