import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/analyze")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setData(data);
      })
      .catch((err) => console.error(err));
  }, []);

  if (!data) {
    return (
      <div
        style={{
          padding: "40px",
          textAlign: "center",
          fontSize: "30px",
        }}
      >
        Loading...
      </div>
    );
  }

  const cardStyle = {
    background: "#f4f4f4",
    padding: "20px",
    borderRadius: "12px",
    marginBottom: "20px",
    color: "#000",
  };

  return (
    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
        maxWidth: "1200px",
        margin: "0 auto",
      }}
    >
      <h1 style={{ textAlign: "center" }}>
        🏥 DuCO Agent Dashboard
      </h1>

      <hr />

      <h2>📄 Document Analysis</h2>

      <div style={cardStyle}>
        <pre
          style={{
            whiteSpace: "pre-wrap",
            overflowX: "auto",
          }}
        >
          {typeof data.documents === "string"
            ? data.documents
            : JSON.stringify(data.documents, null, 2)}
        </pre>
      </div>

      <h2>💰 Coordination of Benefits</h2>

      <div style={cardStyle}>
        <h3>Aarav</h3>

        <p>
          <strong>Total Cost:</strong> ₹{data.cob.aarav.total_cost}
        </p>

        <p>
          <strong>Primary Paid:</strong> ₹{data.cob.aarav.primary_paid}
        </p>

        <p>
          <strong>Secondary Paid:</strong> ₹{data.cob.aarav.secondary_paid}
        </p>

        <p>
          <strong>Out Of Pocket:</strong> ₹{data.cob.aarav.out_of_pocket}
        </p>

        <hr />

        <h3>Priya</h3>

        <p>
          <strong>Total Cost:</strong> ₹{data.cob.priya.total_cost}
        </p>

        <p>
          <strong>Primary Paid:</strong> ₹{data.cob.priya.primary_paid}
        </p>

        <p>
          <strong>Secondary Paid:</strong> ₹{data.cob.priya.secondary_paid}
        </p>

        <p>
          <strong>Out Of Pocket:</strong> ₹{data.cob.priya.out_of_pocket}
        </p>

        <hr />

        <h3>Family Summary</h3>

        <p>
          <strong>Total Out Of Pocket:</strong> ₹
          {data.cob.family_total_oop}
        </p>
      </div>
    </div>
  );
}

export default App;