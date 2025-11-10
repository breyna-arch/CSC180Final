import React from "react";

export default function Loading() {
  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
      }}
    >
      <div
        style={{
          width: 48,
          height: 48,
          border: "4px solid #ccc",
          borderTop: "4px solid #bf1be4ff",
          borderRadius: "50%",
          animation: "spin 1s linear infinite",
        }}
      />
      <p>Loading...</p>

      <style>{`
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}
