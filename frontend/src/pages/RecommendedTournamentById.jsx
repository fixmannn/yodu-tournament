import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import {Container} from 'react-bootstrap';


const RecommendedTournamentById = () => {
  const [data, setData] = useState([]);
  const {user_id} = useParams();


  const fetchData = () => {
    fetch(`/recommended_tournament/${user_id}`)
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
  }, [user_id]);

  return(
    <div>
      {data.hasOwnProperty('message') ? (
        <div className="center-container">
          <h4>{data['message']}</h4>
        </div>
        ) : (
          <div className="center-container">
            <Container>
              <h2 className="text-center mb-4">List of Active Tournament Based on Your Game Team</h2>
              <table className="table table-dark">
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
      )}
    </div>
  )
}

export default RecommendedTournamentById;