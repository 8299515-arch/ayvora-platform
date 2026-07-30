export default function Home() {
  return (
    <main style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1 style={{ fontSize: "48px" }}>
        Ayvora AI Marketplace
      </h1>

      <p style={{ fontSize: "22px" }}>
        Smart dropshipping platform powered by AI
      </p>

      <h2>Featured Products</h2>

      <div style={{
        display: "flex",
        gap: "20px",
        flexWrap: "wrap"
      }}>
        <Product 
          name="Smart Travel Pack" 
          price="79$" 
        />

        <Product 
          name="Ergonomic LED Desk" 
          price="129$" 
        />

        <Product 
          name="Minimal Performance Sneakers" 
          price="64$" 
        />
      </div>
    </main>
  );
}


function Product({
  name,
  price
}: {
  name: string;
  price: string;
}) {
  return (
    <div style={{
      border: "1px solid #ddd",
      borderRadius: "15px",
      padding: "20px",
      width: "250px"
    }}>
      <h3>{name}</h3>
      <p>{price}</p>
      <button>
        Buy now
      </button>
    </div>
  );
}
