import axios from "axios";


export const solveQuestion = async (question) => {

    const API_URL = "http://127.0.0.1:8000/api/solve/";
    try {
        const response = await axios.post(
            API_URL,
            { question },  // ✅ Correct JSON format
            { headers: { "Content-Type": "application/json" } }  // ✅ Ensure JSON request
        );
        return response.data;
    } catch (error) {
        console.error("Error:", error.response?.data || error.message);
        const backendError = error.response?.data?.error;
        return { error: backendError || "Failed to get a response from the server." };
    }
};

export const downloadExcel = async () => {
    const API_URL = "http://127.0.0.1:8000/api/download/";

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to download file");
        }

        // Create a blob object from the response
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);

        // Create a temporary link and trigger the download
        const a = document.createElement("a");
        a.href = url;
        a.download = "leetcode_solutions.xlsx";
        document.body.appendChild(a);
        a.click();

        // Cleanup
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    } catch (error) {
        console.error("Error downloading file:", error);
    }
};