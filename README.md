# 香港郵政局郵件投遞箱地圖

一個互動式網頁應用程式，以地圖形式顯示香港郵政局轄下郵件投遞箱的位置、地址、所屬區域及收箱時間。實際郵箱數量以官方 API 最新資料為準。

## 功能特色

- **互動地圖**：以 Leaflet.js 呈現，使用香港地政總署官方地形圖圖層
- **三層級資料分類**：依「地區 → 分區 → 子分區」三層次組織郵箱資料
- **分區顏色標記**：不同 `district_name_tc` 的郵箱以不同顏色標示，方便識別
- **圖例面板**：右下角可縮放/摺疊的圖例，顯示各分區對應顏色，點擊可快速篩選
- **搜尋功能**：即時搜尋郵箱號碼、地址、地區、分區、子分區
- **彈出資訊**：點擊地圖標記或左側列表項目，顯示郵筒號碼、地區、分區、子分區、地址及最後收箱時間
- **響應式設計**：支援桌面及流動裝置

## 地圖圖層

- **底圖**：[LandsD Topographic Basemap](https://mapapi.geodata.gov.hk/gs/api/v1.0.0/xyz/basemap/WGS84/{z}/{x}/{y}.png) — 香港地政總署官方地形圖
- **地名標籤**：[LandsD Map Label API](https://mapapi.geodata.gov.hk/gs/api/v1.0.0/xyz/label/hk/tc/WGS84/{z}/{x}/{y}.png) — 繁體中文街道名稱及地名

## 資料來源及更新

- 郵箱資料由[香港郵政郵箱網頁](https://webapp.hongkongpost.hk/tc/about_us/network/street_posting_boxes2/index.html#list)使用的官方 API 提供：`https://webapp.hongkongpost.hk/api1/v1/postOffice/all-street-posting-box`
- 整理後的地圖資料存放在 `data/post-boxes.json`，包含郵筒位置及平日、星期六、星期日和公眾假期的收箱時間（來源有提供的時段才會顯示）
- GitHub Actions 每月自動檢查並更新資料；亦可在 GitHub Actions 頁面手動執行 **Update postal-box data**。只有資料有變更時才會建立更新提交。
- 本機可執行 `python extract_mailpost.py` 重新取得資料；此指令亦會更新 `mailpost.txt`。

### 地區分佈

| 地區 | 分區 | 郵箱數目 |
|------|------|----------|
| 港島區 | 南區、灣仔區、中西區、東區 | 310 |
| 九龍區 | 油尖旺區、深水埗區、黃大仙區、九龍城區、觀塘區 | 299 |
| 新界區 | 北區、葵青區、元朗區、沙田區、屯門區、大埔區、西貢區、荃灣區 | 489 |
| 離島區 | 離島區 | 60 |

## 排序規則

左側資料列表依以下層級排序：

1. `region_name_tc`（地區）
2. `district_name_tc`（分區）
3. `sub_district_name_tc`（子分區）
4. `box_no`（郵箱號碼）— 數字依數值大小排序，非數字依繁體中文 locale 排序

## 技術堆疊

- **地圖引擎**：[Leaflet.js](https://leafletjs.com/) v1.9.4
- **圖層來源**：[Lands Department Map API](https://api.portal.hkmapservice.gov.hk/)
- **字型**：[Huninn](https://fonts.googleapis.com/css2?family=Huninn&display=swap)（香港政府常用中文字型）
- **單頁應用**：純靜態網頁，無需建置工具，可由本機 HTTP 伺服器或網站託管服務提供

## 檔案說明

| 檔案 | 說明 |
|------|------|
| `index.html` | 主要網頁檔案（HTML、CSS 及 JavaScript） |
| `data/post-boxes.json` | 網頁載入的郵筒位置及收箱時間資料 |
| `extract_mailpost.py` | 從香港郵政官方 API 擷取及整理郵箱資料 |
| `mailpost.txt` | 郵箱資料的文字格式匯出 |

## 使用方法

1. 以本機 HTTP 伺服器或網站託管服務開啟網頁（網頁會透過 HTTP 載入 `data/post-boxes.json`，不能直接以 `file://` 開啟）
2. 左側欄位可展開查看各區郵箱列表
3. 點擊郵箱項目，地圖會飛往該位置並顯示詳細資訊
4. 使用搜尋框快速過濾郵箱
5. 點擊右下角圖例的分區名稱，可快速顯示該分區所有郵箱

## 授權

地圖圖層資料版權歸 [香港特別行政區政府地政總署](https://api.portal.hkmapservice.gov.hk/disclaimer) 所有。
