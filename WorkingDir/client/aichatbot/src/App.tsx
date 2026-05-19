import AutoAwesomeIcon from "@mui/icons-material/AutoAwesome";
import SendIcon from "@mui/icons-material/Send";
import "./App.css";
import { TextField, Button } from "@mui/material";
import { useState } from "react";

function App() {
  const [chatHistory, setChatHistory] = useState<string[]>([]);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const sendMessage = async (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    if (message && message.trim().length > 0) {
      setChatHistory((prev) => [...prev, message]);
      // Send to our API
      const userMessage = {
        message: message,
      };
      const response = await fetch("http://localhost:8000/chat", {
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userMessage),
        method: "POST",
      });
      setMessage("");
      const data = await response.json();
      setChatHistory((prev) => [...prev, data.reply]);
    } else {
      setError("You have not typed anything...");
    }
  };

  return (
    <>
      <header>
        <div className="text-left m-5 font-bold">AI ChatBot</div>
      </header>
      {chatHistory.length > 0 ? (
        <section className="chatHistorySection">
          {chatHistory.map((message, index) => (
            <p key={index} className={(index+1) % 2 == 0 ? "response" : "query"}>{message}</p>
          ))}
        </section>
      ) : (
        <section className="my-10 main">
          <AutoAwesomeIcon fontSize="large" color="warning"></AutoAwesomeIcon>
          <h1 className="mb-10">Ask me anything</h1>
        </section>
      )}
      {/* {error ?? <p className="text-left">{error}</p>} */}
      <section className="flex justify-center gap-10">
        <TextField
          id="standard-basic"
          label="Type your question here"
          variant="standard"
          className="my-10 w-2xl"
          onChange={(e) => {
            setError("");
            setMessage(e.target.value);
          }}
          value={error ?
            error :
            message}
        />
        <Button
          variant="contained"
          className="w-42.5"
          color="primary"
          endIcon={<SendIcon />}
          onClick={sendMessage}
        >
          Ask
        </Button>
      </section>
    </>
  );
}

export default App;