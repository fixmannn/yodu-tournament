import { Form, Button, Container } from "react-bootstrap";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const JoinTournament = () => {
  const handleFormSubmit = (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const teamId = formData.get("teamId");
    const tournamentId = formData.get("tournamentId");

    fetch(`/join_tournament/${teamId}/${tournamentId}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({})
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        window.location.reload();
      })
      .catch(error => {
        console.error("Error fetching data: ", error);
      })
  }

  const [data, setData] = useState([]);
  const {team_id, tournament_id} = useParams();
  

  const fetchData = () => {
    fetch(`/join_tournament/${team_id}/${tournament_id}`)
    .then(response => response.json())
    .then(data => {
      setData(data);
      console.log(data);
    })
    .catch(error => {
      console.error("Error fetching data: ", error);
    })
  }

  useEffect(() => {
    fetchData()
  }, [team_id, tournament_id]);

  return (
    <div>
      {data['message'] == 'Not registered yet' ?         
      (
        <div className="center-container">
            <h2 className="text-center mb-4">Join the Tournament</h2>
            <Form onSubmit={handleFormSubmit}>
              <Form.Group className="mb-3">
                <Form.Label>Team ID</Form.Label>
                <Form.Control type="text" placeholder="Enter Team ID" style={{width: "400px"}} name="teamId" value={team_id}/>
              </Form.Group>
        
              <Form.Group className="mb-3">
                <Form.Label>Tournament ID</Form.Label>
                <Form.Control type="text" placeholder="Enter Tournament ID" style={{width: "400px"}} name="tournamentId" value={tournament_id}/>
              </Form.Group>
              <Button variant="warning" type="submit" className="text-white">
                Join Tournament
              </Button>
            </Form>
          </div>
        ) : 
        (     
          <div className="center-container">
            <Container>
              <h3 className="text-center mb-4">{data.message}</h3>
              <table className="table table-dark">
                  <thead>
                    <tr>
                      <th scope="col">Team to Tournament ID</th>
                      <th scope="col">Team ID</th>
                      <th scope="col">Tournament ID</th>
                      <th scope="col">Status Daftar</th>
                    </tr>
                  </thead>
                  <tbody>
                      <tr>
                      <th scope="row">{data.team_tournament_id}</th>
                      <td>{data.team_id}</td>
                      <td>{data.tournament_id}</td>
                      <td>{data.status_daftar}</td>
                    </tr>
                  </tbody>
              </table>
            </Container>
          </div>
        )}
    </div>
  );
}

export default JoinTournament;