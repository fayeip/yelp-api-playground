
function BizCard(props) {
    console.log("inside BizCard"); 
    
    return (
        <div className="col">
            <div className="card"> 
                <img src={props.image_url} className="card-img-top" /> 
                <div className="card-body">
                    <h5 className="card-title"> {props.name} </h5>
                    <div className="card-text"> 
                        <p> {props.address_street} <br /> {props.address_city} {props.address_state} {props.address_zip} </p>
                        <p> {props.display_phone} </p> 
                        <p> Rating: {props.rating} </p> 
                        <p> Categories: {props.categories.join(" ")} </p>  
                        <p> Check out their <a href={props.yelp_url}>Yelp review</a>! </p>           
                    </div>
                </div>
            </div>
        </div> 
    ); 

}

function CategoryButton(props) { 
    return (
        <button type="button" className="btn btn-outline-secondary btn-sm m-1">{props.categoryName}</button>
    );
}

function AllBusinessesPage(props) { 
    const allBusinesses = props.businesses; 
    console.log("inside AllBusinessesPage"); 
    const bizCards = []; 

    for (const biz of Object.values(allBusinesses)) {
        const bizCard = (
            <BizCard 
                key={biz.business_id} 
                name={biz.name} 
                image_url={biz.image_url} 
                yelp_url={biz.yelp_url} 
                review_count={biz.review_count} 
                rating={biz.rating} 
                coordinates_latitude={biz.coordinates_latitude} 
                coordinates_longitude={biz.coordinates_longitude} 
                address_street={biz.address_street} 
                address_city={biz.address_city} 
                address_state={biz.address_state} 
                address_zip={biz.address_zip} 
                display_phone={biz.display_phone} 
                categories={biz.categories}
            />
        );
        bizCards.push(bizCard); 
    }

    return (
        <div className="row row-cols-3 row-cols-md-3">
            { bizCards } 
        </div>
    );

}


function Sidebar(props) {
    const activeCategories = props.activeCategories; 
    console.log("inside Sidebar"); 
    const catButtons = []; 

    for (const cat of Object.values(activeCategories)) {
        console.log(cat); 
        const catBtn = (<CategoryButton categoryName={cat.name} />);
        catButtons.push(catBtn); 
    } 

    return (
        <div> {catButtons} </div>
    );
}


function App() {
  const [businesses, setBusinesses] = React.useState({});
  const [activeCategories, setActiveCategories] = React.useState({}); 

  React.useEffect(() => {
    fetch('/api/businesses')
      .then((response) => response.json())
      .then((businesses) => {
        setBusinesses(businesses);
      });
  }, []);

  console.log(businesses);

  React.useEffect(() => {
    fetch('/api/categories')
    .then((response) => response.json())
    .then((activeCategories) => {
      setActiveCategories(activeCategories);
    });
    }, []);

console.log(activeCategories); 


  return (
    <div className="row">
        <div className="col-2" id="sidebar">
        <Sidebar activeCategories={activeCategories} />
        </div>
        <div className="col-10" id="main">
        <AllBusinessesPage businesses={businesses} /> 
        </div>
    </div>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));
