from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.router import router as router_news


app = FastAPI()
app.include_router(router_news)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.post("/news/", response_model=NewsItem)
# def create_news(item: NewsItem):
#     with SessionLocal() as session:  # Исправлено на SessionLocal()
#         news_entry = NewTable(id=item.id, var1=item.var1, var2=item.var2)
#         session.add(news_entry)
#         session.commit()
#         session.refresh(news_entry)
#         return news_entry


# @app.get("/news/{news_id}", response_model=NewsItem)
# def read_news(news_id: int):
#     with SessionLocal() as session:
#         news_entry = session.query(NewTable).filter(NewTable.id == news_id).first()
#         if news_entry is None:
#             raise HTTPException(status_code=404, detail="News item not found")
#         return news_entry


# @app.put("/news/{news_id}", response_model=NewsItem)
# def update_news(news_id: int, item: NewsItem):
#     with SessionLocal() as session:
#         news_entry = session.query(NewTable).filter(NewTable.id == news_id).first()
#         if news_entry is None:
#             raise HTTPException(status_code=404, detail="News item not found")
#         news_entry.var1 = item.var1
#         news_entry.var2 = item.var2
#         session.commit()
#         return NewsItem(id=news_entry.id, var1=news_entry.var1, var2=news_entry.var2)


# @app.delete("/news/{news_id}", response_model=dict)
# def delete_news(news_id: int):
#     with SessionLocal() as session:
#         news_entry = session.query(NewTable).filter(NewTable.id == news_id).first()
#         if news_entry is None:
#             raise HTTPException(status_code=404, detail="News item not found")
#         session.delete(news_entry)
#         session.commit()
#         return {"detail": "News item deleted"}
