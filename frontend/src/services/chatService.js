class ChatService {
  constructor(apiBaseUrl = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api/v1') {
    this.apiBaseUrl = apiBaseUrl;
  }

  async sendMessage(query, sessionId = null, selectedText = null) {
    try {
      const response = await fetch(`${this.apiBaseUrl}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query,
          session_id: sessionId,
          selected_text: selectedText,
          temperature: 0.7
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error sending message:', error);
      throw error;
    }
  }

  async getHealth() {
    try {
      const response = await fetch(`${this.apiBaseUrl}/health`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error getting health:', error);
      throw error;
    }
  }

  async getStatus() {
    try {
      const response = await fetch(`${this.apiBaseUrl}/status`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error getting status:', error);
      throw error;
    }
  }
}

export default new ChatService();