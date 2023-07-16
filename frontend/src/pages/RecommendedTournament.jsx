import { useState, useEffect } from "react";
import { Container } from "react-bootstrap";

const RecommendedTournament = () => {
  const [data, setData] = useState([]);


  const fetchData = () => {
    fetch("/recommended_tournament")
    .then(response => response.json())
    .then(data => {
      setData(data);
      console.log(data)
    })
    .catch(error => {
      console.error("Error fetching data: ", error);
    })
  }

  useEffect(() => {
    fetchData()
  }, []);

  return(
    <div className="center-container">
      <Container>
        <h2 className="text-center mb-4">List of Active Tournament</h2>
        <table className="table table-dark rounded">
          <thead>
            <tr>
              <th scope="col">Tournament ID</th>
              <th scope="col">Tournament Name</th>
              <th scope="col">Game</th>
              <th scope="col">Status</th>
              <th scope="col">Team Registered</th>
            </tr>
          </thead>
          <tbody>
            {data.map(item => (
              <tr>
              <th scope="row">{item.tourney_id}</th>
              <td>{item.tournament_name}</td>
              <td>{item.games.game_name}</td>
              <td>{item.status}</td>
              <td>{item.teams.map(team => (
                <span key={team.team_id}>{team.team_name}, </span>
              ))}</td>
            </tr>
            ))}
          </tbody>
        </table>
      </Container>
    </div>
  )
}

export default RecommendedTournament;