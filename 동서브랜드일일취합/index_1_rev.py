<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>동서가구 브랜드 판매</title>
    <link href="index3.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
    <style>
        /* tooltip */
        .tooltip {
        position: absolute;
        top: -30px;
        left: 10px;
        background-color: #000;
        color: #fff;
        padding: 5px;
        border-radius: 5px;
        z-index: 9999;
        display: none;
        }
        /* 베스트제품 */
        #best {
            display: flex;
            flex-direction: row; 
            flex-wrap: wrap;
        }

        /* 카드 형식 */
        .best_card {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px;
            width: 200px;
        }

        /* 커서 올렸을 때 그림자 */
        .best_card:hover {
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2), 0 6px 6px rgba(0, 0, 0, 0.2);
        }

        .best_card h2 {
            font-size: 14px;
            margin: 0 0 10px;
        }

        .best_card img {
            margin-bottom: 10px;
        }

        .best_card p {
            font-size: 14px;
            margin: 0;
        }

        /* 판매순 */
        #btn_ea_1w,
        #btn_ea_2w,
        #btn_ea_3w,
        #btn_ea_1m,
        #btn_ea_3m,
        #btn_ea_6m {
            background-color: rgb(194, 194, 243);
            color: rgb(255, 255, 255);
            border: none;
        }

        #btn_ea_1w:hover,
        #btn_ea_2w:hover,
        #btn_ea_3w:hover,
        #btn_ea_1m:hover,
        #btn_ea_3m:hover,
        #btn_ea_6m:hover {
            background-color: darkblue;
        }

        /* 금액순 */
        #btn_pr_1w,
        #btn_pr_2w,
        #btn_pr_3w,
        #btn_pr_1m,
        #btn_pr_3m,
        #btn_pr_6m {
            background-color: rgb(241, 160, 179);
            color: white;
            border: none;
        }

        #btn_pr_1w:hover,
        #btn_pr_2w:hover,
        #btn_pr_3w:hover,
        #btn_pr_1m:hover,
        #btn_pr_3m:hover,
        #btn_pr_6m:hover {
            background-color: rgb(139, 0, 97);
        }

        .btn-ea {
            background-color: rgb(194, 194, 243);
            color: white;
            border: none;
        }

    </style>
</head>

<body>
    <div id="target">cursor</div>
    <div class="cards-list">
        <a style="text-decoration: none;">  <!-- 밑줄이 없는 글자 -->
            <div class="card 1" onclick="best('btn_pr_6m');" style="background-color: rgb(243, 98, 72);">
                <div class="card_title title-black"> <!-- css -->
                    <br>BEST
                </div>
            </div>
        </a>
        <a style="text-decoration: none;">
            <div class="card 1" onclick="inni(10);" style="background-color: rgb(167, 255, 95);">
                <div class="card_title title-black">
                    <br>실시간
                </div>
            </div>
        </a>
        <a style="text-decoration: none">
            <div class="card 1" onclick="inni(1);">
                <div class="card_title title-black">
                    <br>어제
                </div>
            </div>
        </a>
        <a style="text-decoration: none">
            <div class="card 2" onclick="inni(0);">
                <div class="card_title title-black">
                    <br>오늘
                </div>
            </div>
        </a>
        <a style="text-decoration: none">
            <div class="card 3" onclick="inni(7);">
                <div class="card_title title-black">
                    <br>7일
                </div>
            </div>
        </a>
        <a style="text-decoration: none">
            <div class="card 4" onclick="inni(11);">
                <div class="card_title title-black">
                    <br>한달
                </div>
            </div>
        </a>
        <a style="text-decoration: none">
            <div class="card 5" onclick="inni(33);">
                <div class="card_title title-black">
                    <br>3달
                </div>
            </div>
        </a>
        <a style="text-decoration: none">
            <div class="card 5" onclick="inni(66);">
                <div class="card_title title-blck">
                    <br>6달
                </div>
            </div>
        </a>
    </div>
    <div>
        <input id="input_start" type="date"></input>~<input id="input_end" type="date">
        <input id="input_submit" class="warning" type="submit" onclick="inni(999);" value="검색">
        <div class="dim"></div>
    </div>
    <div class="wrap_box">
        <div id="part_btn"></div>
        <div id="part_chart1"></div>
        <div id="part_chart2"></div>
        <div id="part_list"></div>
    </div>



    <script>

        function best(choice) {
            //데이터 들고오기 메인데이터
            var url = "brand_1.csv"
            axios
                .get(url)
                .then(function (result) {
                    var my_str = result.data.replaceAll('\r', '');
                    var tableData = my_str.split('\n')
                    tableData = tableData.slice(0, -1);
                    for (i = 0; i < tableData.length; i++) {
                        tableData[i] = tableData[i].split(",");
                        tableData[i][3] = tableData[i][3].split("#")[0];
                    }
                    // console.log(tableData);

                    function formatDate(date) {
                        var year = date.getFullYear();
                        var month = String(date.getMonth() + 1).padStart(2, '0');
                        var day = String(date.getDate()).padStart(2, '0'); //날짜
                        return year + '-' + month + '-' + day;
                    } 

                    function getDateWeeksAgo(weeks) {
                        var currentDate = new Date();
                        var pastDate = new Date(currentDate.getTime() - weeks * 7 * 24 * 60 * 60 * 1000);
                        return formatDate(pastDate);
                    }

                    function getDateMonthsAgo(months) {
                        var currentDate = new Date();
                        var pastDate = new Date(currentDate.getFullYear(), currentDate.getMonth() - months, currentDate.getDate());
                        return formatDate(pastDate);
                    }

                    // Get today's date
                    var currentDate = new Date();
                    var formattedDate = formatDate(currentDate);
                    // console.log("Today's date: " + formattedDate);

                    // Get dates from the past
                    var oneWeekAgo = getDateWeeksAgo(1);
                    var twoWeeksAgo = getDateWeeksAgo(2);
                    var threeWeeksAgo = getDateWeeksAgo(3);
                    var oneMonthAgo = getDateMonthsAgo(1);
                    var threeMonthsAgo = getDateMonthsAgo(3);
                    var sixMonthsAgo = getDateMonthsAgo(6);


                    //삭제, 재생성
                    var wrap_box = document.querySelector('.wrap_box');

                    var durations = [
                        { id: 'btn_ea_1w', text: '1주간 판매순' },
                        { id: 'btn_ea_2w', text: '2주간 판매순' },
                        { id: 'btn_ea_3w', text: '3주간 판매순' },
                        { id: 'btn_ea_1m', text: '1달간 판매순' },
                        { id: 'btn_ea_3m', text: '3달간 판매순' },
                        { id: 'btn_ea_6m', text: '6달간 판매순' }
                        ];

                        for (var i = 0; i < durations.length; i++) {
                        var duration = durations[i];

                        var rmv = document.getElementById(duration.id);
                        if (rmv) rmv.parentNode.removeChild(rmv);

                        var button = document.createElement('button');
                        button.setAttribute('id', duration.id);
                        button.setAttribute('type', 'button');
                        button.setAttribute('onclick', 'best("' + duration.id + '")');
                        button.innerText = duration.text;

                        wrap_box.appendChild(button);
                        }

                    
                    function date_cal(duration) {
                        var endDate = new Date(duration);
                        tableData = tableData.filter(row => {
                            var rowDate = new Date(row[0]);
                            return endDate <= rowDate && rowDate <= currentDate;
                        });
                        console.log(tableData);
                        console.log(tableData[0][0])
                    }

                    //button control (1w, 2w, 3w, 1m, 3m, 6m)
                    if (choice == "btn_ea_1w" || choice == "btn_pr_1w") {
                        date_cal(oneWeekAgo)
                    }
                    else if (choice == "btn_ea_2w" || choice == "btn_pr_2w") {
                        date_cal(twoWeeksAgo)
                    }
                    else if (choice == "btn_ea_3w" || choice == "btn_pr_3w") {
                        date_cal(threeWeeksAgo)
                    }
                    else if (choice == "btn_ea_1m" || choice == "btn_pr_1m") {
                        date_cal(oneMonthAgo)
                    }
                    else if (choice == "btn_ea_3m" || choice == "btn_pr_3m") {
                        date_cal(threeMonthsAgo)
                    }
                    else if (choice == "btn_ea_6m" || choice == "btn_pr_6m") {
                        date_cal(sixMonthsAgo)
                    }


                    var rmv = document.getElementById("part_btn");
                    if (rmv) rmv.parentNode.removeChild(rmv);
                    var part_btn = document.createElement('div')
                    part_btn.setAttribute('id', 'part_btn');
                    wrap_box.appendChild(part_btn)

                    var rmv = document.getElementById("part_chart1");
                    if (rmv) rmv.parentNode.removeChild(rmv);
                    var part_chart1 = document.createElement('div')
                    part_chart1.setAttribute('id', 'part_chart1');
                    wrap_box.appendChild(part_chart1)

                    var rmv = document.getElementById("part_chart2");
                    if (rmv) rmv.parentNode.removeChild(rmv);
                    var part_chart2 = document.createElement('div')
                    part_chart2.setAttribute('id', 'part_chart2');
                    wrap_box.appendChild(part_chart2)


                    var rmv = document.getElementById("btn_div");
                    if (rmv) rmv.parentNode.removeChild(rmv);
                    var btn_div = document.createElement('div')
                    btn_div.setAttribute('id', 'btn_div');
                    wrap_box.appendChild(btn_div)

                    var rmv = document.getElementById("part_list");
                    if (rmv) rmv.parentNode.removeChild(rmv);
                    var btn_div = document.createElement('div')
                    btn_div.setAttribute('id', 'part_list');
                    wrap_box.appendChild(btn_div)

                    var rmv = document.getElementById("best");
                    if (rmv) rmv.parentNode.removeChild(rmv);
                    var cardContainer = document.createElement('div');
                    cardContainer.setAttribute('id', 'best');
                    wrap_box.appendChild(cardContainer)

                    //
                    var choice_menu = document.createElement('div');
                    choice_menu.setAttribute('id', 'choice_menu');
                    cardContainer.appendChild(choice_menu);

                    const tableData2 = [];
                    const tempObj = {};

                    for (let i = 0; i < tableData.length; i++) {
                        const productName = tableData[i][3];
                        if (tempObj[productName] === undefined) {
                            tempObj[productName] = {
                                productName: productName,
                                quantity: parseInt(tableData[i][4]),
                                price: parseInt(tableData[i][5]),
                                status: tableData[i][6],
                                imgUrl: tableData[i][2],
                                shopName: tableData[i][1]
                            };
                        } else {
                            tempObj[productName].quantity += parseInt(tableData[i][4]);
                            tempObj[productName].price += parseInt(tableData[i][5]);
                        }
                    }

                    for (const key in tempObj) {
                        tableData2.push([tempObj[key].productName, tempObj[key].quantity, tempObj[key].price, tempObj[key].status, tempObj[key].imgUrl, tempObj[key].shopName]);
                    }

                    //매트리스 삭제
                    let indexToDelete = -1;
                    for (let i = 0; i < tableData2.length; i++) {
                        if (tableData2[i][0] == '매트리스 ') {
                            console.log(tableData2[i][0])
                            indexToDelete = i;
                            break;
                        }
                    }
                    if (indexToDelete > -1) {
                        tableData2.splice(indexToDelete, 1);
                    }

                    //판매순 tableData_cnt
                    const tableData_cnt = tableData2.slice().sort(function (a, b) {
                        return b[1] - a[1];
                    });

                    //판매금액순 tableData_price
                    const tableData_price = tableData2.slice().sort(function (a, b) {
                        return b[2] - a[2];
                    });

                    if (choice.includes("_ea_") > 0) {
                        // console.log(tableData_cnt);
                        for (let i = 0; i < tableData_cnt.length; i++) {
                            // Create a card element
                            const card = document.createElement('div');
                            card.classList.add('best_card');

                            // Create an image element
                            const image = document.createElement('img');
                            image.setAttribute('src', tableData_cnt[i][4].split("#")[0]);
                            image.setAttribute('width', '200');
                            image.setAttribute('height', '200');
                            const link = document.createElement('a');
                            link.setAttribute('href', tableData_cnt[i][4].split("#")[1]);
                            link.setAttribute('target', '_blank');
                            link.appendChild(image);
                            card.appendChild(link);

                            // Create a title element
                            const title = document.createElement('h2');
                            title.innerText = `${i + 1}. [${tableData_cnt[i][5]}] ${tableData_cnt[i][0]}`;
                            card.appendChild(title);

                            // Create a price element
                            const ea = document.createElement('p');
                            ea.innerText = `판매수량: ${tableData_cnt[i][1].toLocaleString()}개`;
                            ea.setAttribute('style', 'font-weight:bold; color:red');
                            card.appendChild(ea);

                            // Create a price element
                            const price = document.createElement('p');
                            price.innerText = `판매가격: ${tableData_cnt[i][2].toLocaleString()}원`;
                            card.appendChild(price);

                            // Create a price element
                            const ea_price = document.createElement('p');
                            var ea_price_cal = Number(tableData_cnt[i][2]) / Number(tableData_cnt[i][1]);
                            ea_price_cal = Math.round(ea_price_cal / 100) * 100;
                            ea_price.innerText = `개당평균: ${ea_price_cal.toLocaleString()}원`;
                            card.appendChild(ea_price);

                            // Add the card to the container
                            cardContainer.appendChild(card);
                        }
                    }
                    else if (choice.includes("_pr_") > 0) {
                        // console.log(tableData_price);
                        for (let i = 0; i < tableData_price.length; i++) {
                            // Create a card element
                            const card = document.createElement('div');
                            card.classList.add('best_card');

                            // Create an image element
                            const image = document.createElement('img');
                            image.setAttribute('src', tableData_price[i][4].split("#")[0]);
                            image.setAttribute('width', '200');
                            image.setAttribute('height', '200');
                            const link = document.createElement('a');
                            link.setAttribute('href', tableData_price[i][4].split("#")[1]);
                            link.setAttribute('target', '_blank');
                            link.appendChild(image);
                            card.appendChild(link);

                            // Create a title element
                            const title = document.createElement('h2');
                            title.innerText = `${i + 1}. [${tableData_price[i][5]}] ${tableData_price[i][0]}`;
                            card.appendChild(title);

                            // Create a price element
                            const price = document.createElement('p');
                            price.innerText = `판매가격: ${tableData_price[i][2].toLocaleString()}원`;
                            price.setAttribute('style', 'font-weight:bold; color:red');
                            card.appendChild(price);

                            // Create a price element
                            const ea = document.createElement('p');
                            ea.innerText = `판매수량: ${tableData_price[i][1].toLocaleString()}개`;
                            card.appendChild(ea);

                            // Create a price element
                            const ea_price = document.createElement('p');
                            var ea_price_cal = Number(tableData_price[i][2]) / Number(tableData_price[i][1]);
                            ea_price_cal = Math.round(ea_price_cal / 100) * 100;
                            ea_price.innerText = `개당평균: ${ea_price_cal.toLocaleString()}원`;
                            card.appendChild(ea_price);

                            // Add the card to the container
                            cardContainer.appendChild(card);

                            let tooltip = null;

                            function showTooltip(event) {
                                if (tooltip) {
                                    return;
                                }
                                
                                tooltip = document.createElement('div');
                                tooltip.classList.add('tooltip');
                                tooltip.textContent = event.target.title;
                                
                                const x = event.clientX + 10;
                                const y = event.clientY - 20;
                                
                                tooltip.style.left = x + 'px';
                                tooltip.style.top = y + 'px';
                                
                                document.body.appendChild(tooltip);
                            }

                            function hideTooltip() {
                                if (tooltip) {
                                    tooltip.remove();
                                    tooltip = null;
                                }
                            }

                            const bestCards = document.querySelectorAll('.best_card');

                            bestCards.forEach((bestCard) => {
                                const image = bestCard.querySelector('img');

                                image.addEventListener('mouseover', showTooltip);
                                image.addEventListener('mouseout', hideTooltip);
                            });

                                });
                        }
                    }
                })
        }


        function main(ck, skip, filter_date, filter_cp) {
            function showZoomWindow(event) {
            const zoomWindow = document.getElementsByClassName('list_img_src');
            zoomWindow.style.display = 'block';
            zoomWindow.style.top = `${event.clientY}px`;
            zoomWindow.style.left = `${event.clientX + 10}px`;
            }

            function hideZoomWindow() {
            const zoomWindow = document.getElementsByClassName('list_img_src');
            zoomWindow.style.display = 'none';
            }
            const btn_filter = [filter_cp];

            // function js(){
            //     //팝업창출력
            //     //width : 300px크기
            //     //height : 300px크기
            //     //top : 100px 위의 화면과 100px 차이해서 위치
            //     //left : 100px 왼쪽화면과 100px 차이해서 위치
            //     //툴바 X, 메뉴바 X, 스크롤바 X , 크기조절 X
            //     window.open('http://www.naver.com','popName',
            //                 'width=300,height=300,top=100,left=100,toolbar=no,menubar=no,scrollbars=no,resizable=no,status=no');
            //     }

            //실시간 데이터(10)
            if (skip == '10') {
                filter_date = filter_date[filter_date.length - 1]
                console.log(filter_date);
            }

            //데이터 들고오기 메인데이터
            var url = "brand_1.csv"
            axios
                .get(url)
                .then(function (result) {
                    var my_str = result.data.replaceAll('\r', '');
                    var tableData = my_str.split('\n')

                    for (var i = 0; i < tableData.length; i++) {
                        tableData[i] = tableData[i].split(',')
                        tableData[i] = tableData[i].reduce((accumulator, value, index) => {
                            return { ...accumulator, ['key' + index]: value };
                        }, {});
                    }
                    tableData = tableData.slice(0, -1);
                    // console.log(tableData);




                    //업체 클릭시 동작
                    if (btn_filter[0] != '' && btn_filter[0].includes("모두보기") == 0) {
                        //console.log(btn_filter[0])
                        filter_cp = btn_filter;
                        var tableData = tableData.filter(item => filter_date.includes(item.key0) && filter_cp.includes(item.key1))
                    }
                    else {
                        //실시간 데이터(10)
                        if (skip == '10') {
                            var tableData = tableData.filter(item => filter_date.includes(item.key8))
                        } else {
                            var tableData = tableData.filter(item => filter_date.includes(item.key0))
                        }
                        //console.log(tableData)



                        //업체 filter_cp 생성 & 버튼생성
                        //btn 삭제
                        var rmv = document.getElementById("btn_div");
                        if (rmv) rmv.parentNode.removeChild(rmv);

                        var filter_cp = Array.from((new Set(tableData.map(item => item.key1))))
                        filter_cp.push('모두보기')

                        var btn_div = document.createElement('div')
                        btn_div.setAttribute("id", "btn_div")

                        var get_id = document.getElementById("part_btn")
                        get_id.appendChild(btn_div)

                        // for (var i = 0; i < filter_cp.length; i++) {
                        //실시간 데이터(10)
                        if (skip != '10') {
                            for (var i = filter_cp.length - 1; i >= 0; i--) {
                                var button = document.createElement('button')
                                button.setAttribute("id", "my_button")
                                if (filter_cp[i] == '모두보기') {
                                    button.setAttribute("onclick", `main('btn','${skip}','${filter_date}','${filter_cp}');`)
                                } else {
                                    button.setAttribute("onclick", `main('btn','${skip}','${filter_date}','${filter_cp[i]}');`)
                                }
                                button.appendChild(document.createTextNode(filter_cp[i]));
                                btn_div.appendChild(button)
                            }
                        }
                    }
                    //console.log(tableData)
                    //console.log(filter_cp)

                    //chart1
                    //chart1
                    //chart1
                    //chart1
                    if (typeof (filter_date) == "string") {
                        var listDate = filter_date.split(",");
                    } else {
                        var listDate = filter_date
                    }
                    if (ck != 'btn') {

                        //chart 삭제
                        var rmv = document.getElementById("chartContainer");
                        if (rmv) rmv.parentNode.removeChild(rmv);


                        //console.log(listDate)

                        filter_cp = filter_cp.filter(function (data) { return data != "모두보기"; });
                        var sum_all = 0;
                        var EA_all = 0;
                        for (var i = 0; i < filter_cp.length; i++) {
                            var price_temp = 0;
                            var EA_temp = 0;
                            for (var j = 0; j < tableData.length; j++) {
                                if (filter_cp[i] == tableData[j].key1) {
                                    price_temp += Number(tableData[j].key5);
                                    EA_temp += Number(tableData[j].key4);
                                }

                            }
                            sum_all += price_temp;
                            EA_all += EA_temp;
                            filter_cp[i] = { label: `${filter_cp[i]} (${EA_temp})`, y: price_temp / 10000, x: i };
                        }
                        //console.log(filter_cp)
                        var sum_all = String(EA_all) + "건 / " + String(sum_all.toLocaleString('ko-KR')) + "원"

                        var chart_set = document.createElement("div");
                        chart_set.setAttribute("id", "chartContainer");

                        if (filter_cp.length == 1) { var height = "200" } else { var height = "350" }
                        chart_set.setAttribute("style", `height: ${height}px; width: 98.6%;`);

                        var get_chart1 = document.getElementById("part_chart1")
                        get_chart1.appendChild(chart_set);

                        //실시간 데이터(10)
                        if (skip == 0 || skip == 1 || skip == 10 || listDate.length == 1) {
                            text = `${listDate[0]}`
                        } else {
                            text = `${listDate[0]} ~ ${listDate[listDate.length - 1]}`
                        }

                        var chart = new CanvasJS.Chart("chartContainer", {
                            theme: "light1", // "light1", "light2", "dark1"
                            animationEnabled: true,
                            //exportEnabled: true,
                            title: {
                                margin: 10,
                                text: text
                            },
                            axisX: {
                                //margin: 50,
                                labelPlacement: "outside",
                                tickPlacement: "inside"
                            },
                            axisY2: {
                                title: sum_all,
                                titleFontSize: 20,
                                includeZero: true,
                                suffix: ""
                            },
                            data: [{
                                type: "bar",
                                axisYType: "secondary",
                                yValueFormatString: "#,###만원",
                                indexLabel: "{y}",
                                dataPoints: filter_cp
                            }]
                        });
                        chart.render();
                    }



                    //chart2
                    //chart2
                    //chart2
                    //chart2

                    //chart2 삭제
                    var rmv = document.getElementById("chartContainer2");
                    if (rmv) rmv.parentNode.removeChild(rmv);

                    // 2일 이상 표시
                    //실시간 데이터(10)
                    if (Number(skip) > 1 && Number(skip) != 10) {
                        //console.log(filter_date);
                        //console.log(tableData);
                        //console.log(skip);

                        if (typeof (filter_date) == "string") {
                            var listDate = filter_date.split(",");
                        } else {
                            var listDate = filter_date
                        }
                        //console.log(listDate)


                        var chart2Data1 = new Array
                        var chart2Data2 = new Array
                        var all_EA = 0;
                        var all_margin = 0;
                        for (var i = 0; i < listDate.length; i++) {
                            var EA = 0;
                            var margin = 0;
                            for (var j = 0; j < tableData.length; j++) {
                                if (listDate[i] == tableData[j].key0) {
                                    EA += Number(tableData[j].key4);
                                    margin += Number(tableData[j].key5);
                                }
                            }
                            all_EA += EA;
                            all_margin += margin;

                            var year = Number(listDate[i].substring(0, 4));
                            var month = ('00' + Number(listDate[i].substring(5, 7))).slice(-2) - 1;
                            var day = ('00' + Number(listDate[i].substring(8, 10))).slice(-2);
                            chart2Data1.push({ x: new Date(year, month, day), y: EA });
                            chart2Data2.push({ x: new Date(year, month, day), y: margin });
                        }
                        // console.log(chart2Data1)
                        // console.log(chart2Data2)

                        // console.log(all_EA);
                        // console.log(all_margin);

                        //chart2 생성
                        var chart_set = document.createElement("div");
                        chart_set.setAttribute("id", "chartContainer2");
                        chart_set.setAttribute("style", "height: 200px; width: 99%;")

                        var get_chart2 = document.getElementById("part_chart2");
                        get_chart2.append(chart_set);


                        // sub_title
                        if (filter_cp.length > 1) {
                            var title = ''
                        } else {
                            title = filter_cp[0];
                            title = `[${title}] ${all_EA}건 ${all_margin.toLocaleString('ko-KR')}원`
                        }

                        var chart = new CanvasJS.Chart("chartContainer2", {
                            subtitles: [{
                                text: title,
                                fontFamily: "arial black",
                                fontColor: "#000000",
                                margin: 10,
                                fontSize: 17,
                                fontWeight: "bold"
                            }],
                            axisX: {
                                interval: 1,
                                valueFormatString: "MM.DD(DDD)",
                                labelFontSize: 12,
                                labelFontColor: "#000000",
                                // labelFontWeight: "bold"
                            },
                            toolTip: {
                                shared: true
                            },
                            legend: {
                                cursor: "pointer",
                                itemclick: toggleDataSeries
                            },
                            data: [{
                                type: "column",
                                name: "판매금액",
                                color: "#FFC3A1",
                                showInLegend: true,
                                axisYIndex: 0,
                                dataPoints: chart2Data2
                            },
                            {
                                type: "line",
                                name: "판매수",
                                color: "#FFFFFF",
                                // axisYType: "secondary",
                                // showInLegend: true,
                                dataPoints: chart2Data1
                            }
                            ]
                        });
                        chart.render();

                        function toggleDataSeries(e) {
                            if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                                e.dataSeries.visible = false;
                            } else {
                                e.dataSeries.visible = true;
                            }
                            e.chart.render();
                        }
                    }





                    //list
                    //list
                    //list
                    //list
                    for (var i = 0; i < tableData.length; i++) {
                        var strArr = [];
                        for (let objKey in tableData[i]) {
                            if (tableData[i].hasOwnProperty(objKey)) {
                                strArr.push(tableData[i][objKey]);
                            }
                        }
                        tableData[i] = strArr
                    }
                    //console.log(tableData);


                    //list 삭제
                    remove_list = ['myTable', 'myBr', 'best', 'btn_ea_1w', 'btn_ea_2w', 'btn_ea_3w', 'btn_ea_1m', 'btn_ea_3m', 'btn_ea_6m', 'btn_pr_1w', 'btn_pr_2w', 'btn_pr_3w', 'btn_pr_1m', 'btn_pr_3m', 'btn_pr_6m']
                    for (rm = 0; rm < remove_list.length; rm++) {
                        var rmv = document.getElementById(remove_list[rm]);
                        if (rmv) rmv.parentNode.removeChild(rmv);
                    }

                    var get_list = document.getElementById("part_list");

                    //<br>
                    var br = document.createElement('br');
                    br.setAttribute("id", "myBr");
                    get_list.appendChild(br)

                    //<table>
                    var table = document.createElement('table');
                    table.setAttribute("id", "myTable");
                    table.setAttribute("border", "0");
                    table.setAttribute("cellspacing", "0");
                    table.setAttribute("width", "900");
                    get_list.appendChild(table);

                    //<tbody>
                    var tbody = document.createElement('tbody');
                    table.appendChild(tbody);

                    var list_cnt = -1; //리스트카운트
                    function list_show(list_cnt) {
                        //<tr> id=tr_list
                        var tr = document.createElement('tr');
                        tr.setAttribute("id", "myList");
                        tr.setAttribute("align", "center");
                        tr.setAttribute("style", "word-break: break-all");
                        tr.setAttribute("valign", "middle");
                        tbody.appendChild(tr);

                        //<td>
                        var td = document.createElement('td');
                        td.setAttribute("align", "left");
                        tr.appendChild(td);

                        //<table>_img
                        var table_img = document.createElement('table');
                        table_img.setAttribute("border", "0");
                        table_img.setAttribute("cellpadding", "0");
                        table_img.setAttribute("cellspacing", "0");
                        table_img.setAttribute("height", "100%");
                        table_img.setAttribute("width", "100%");
                        table_img.setAttribute("style", "table-layout:fixed");
                        td.appendChild(table_img);

                        //<tbody>_img
                        var tbody_img = document.createElement('tbody');
                        table_img.appendChild(tbody_img);


                        //<tr>_img
                        var tr_img = document.createElement('tr');
                        tbody_img.appendChild(tr_img);

                        //<td>_img
                        var td_img = document.createElement('td');
                        td_img.setAttribute("align", "right");
                        td_img.setAttribute("valign", "top");
                        td_img.setAttribute("width", "75");
                        td_img.setAttribute("style", "padding:0 5px 0 0");
                        tr_img.appendChild(td_img);

                        //<a>_img
                        var a_img = document.createElement('a');
                        a_img.setAttribute("href", (tableData[i][2] || '').split('#')[1]);
                        a_img.setAttribute("target", "_blank");
                        a_img.setAttribute("class", "list_img_href");
                        td_img.appendChild(a_img);

                        //<img>
                        var img = document.createElement('img');
                        img.setAttribute("src", (tableData[i][2] || '').split('#')[0]);
                        img.setAttribute("class", "list_img_src");
                        img.setAttribute("width", "60");
                        img.setAttribute("height", "60");
                        img.setAttribute("border", "0");
                        img.setAttribute("style", "margin:0px 5px 0px 5px;");
                        img.setAttribute("align", "absmiddle");
                        img.setAttribute("onmouseover","js()")
                        img.setAttribute("onmouseout","hideZoomWindow(img)")

                        a_img.appendChild(img)

                        //<td>_title
                        var td_title = document.createElement('td');
                        td_title.setAttribute("valign", "middle")
                        tr_img.appendChild(td_title)

                        //<div>_title
                        var div_title = document.createElement('div');
                        div_title.setAttribute("style", "inline-block;line-height:1.6;vertical-align:middle;line-height:1;")
                        td_title.appendChild(div_title);

                        //<span>_cpy
                        var span_cpy = document.createElement('span');
                        span_cpy.setAttribute("id", "cpy" + String(list_cnt));
                        span_cpy.setAttribute("class", "cpy");
                        span_cpy.setAttribute("style", "inline-block;line-height:1.6;vertical-align:middle;line-height:1;color:#3333FF;font-size:12px;font-weight: bolder;");
                        span_cpy.appendChild(document.createTextNode(tableData[i][1] + "\u00a0"));
                        div_title.appendChild(span_cpy);

                        //<a>_title
                        var a_title = document.createElement('a');
                        a_title.setAttribute("href", (tableData[i][2] || '').split('#')[1]);
                        a_title.setAttribute("target", "_blank");
                        a_title.setAttribute("style", "text-decoration-line: none;inline-block;line-height:1.6;vertical-align:middle;line-height:1;color:#3D5656;font-size:12px;");
                        a_title.setAttribute("id", "list_title" + String(list_cnt));
                        a_title.setAttribute("class", "list_title");
                        a_title.appendChild(document.createTextNode((tableData[i][3] || '').split('#')[0]));
                        div_title.appendChild(a_title);

                        //<br>
                        var br = document.createElement('br');
                        div_title.appendChild(br)

                        //<span>_option
                        var span_option = document.createElement('span');
                        span_option.setAttribute("style", "inline-block;line-height:1.6;vertical-align:middle;line-height:1;color:#999;font-size:11px;");
                        span_option.appendChild(document.createTextNode((tableData[i][3] || '').split('#')[1]));
                        div_title.appendChild(span_option);

                        //<br>
                        var br = document.createElement('br');
                        span_option.appendChild(br)

                        //<span>_date
                        var span_date = document.createElement('span');
                        span_date.setAttribute("style", "inline-block;line-height:1.6;vertical-align:middle;line-height:1;color:#68B984;font-size:11px;");
                        span_date.appendChild(document.createTextNode(tableData[i][8] + "\u00a0"));
                        div_title.appendChild(span_date);

                        //<span>_time
                        var span_time = document.createElement('span');
                        span_time.setAttribute("style", "inline-block;line-height:1.6;vertical-align:middle;line-height:1;color:#CCCCCC;font-size:11px;");
                        span_time.appendChild(document.createTextNode(tableData[i][7] + "\u00a0"));
                        div_title.appendChild(span_time);

                        //<span>_EA
                        var span_EA = document.createElement('span');
                        span_EA.setAttribute("id", "span_EA" + String(list_cnt));
                        span_EA.setAttribute("class", "span_EA");
                        span_EA.appendChild(document.createTextNode(tableData[i][4]));
                        div_title.appendChild(span_EA);

                        //<span>_price
                        var span_price = document.createElement('span');
                        span_price.setAttribute("id", "price" + String(list_cnt));
                        span_price.setAttribute("class", "price");
                        span_price.setAttribute("style", "inline-block;line-height:1.6;vertical-align:middle;line-height:1;color:#FD8A8A;font-size:11px;");
                        span_price.appendChild(document.createTextNode("\u00a0" + Number(tableData[i][5]).toLocaleString() + "원"));
                        div_title.appendChild(span_price);
                    }
                    for (var i = 0; i < tableData.length; i++) {
                        for (var d = 0; d < listDate.length; d++) {
                            //실시간 데이터(10)
                            if (skip == '10' && listDate[d] == tableData[i][8]) {
                                list_cnt += 1; //리스트카운트
                                list_show(list_cnt);
                                //그 외
                            } else if (listDate[d] == tableData[i][0]) {
                                list_cnt += 1; //리스트카운트
                                list_show(list_cnt);
                            }
                        }
                    }
                })
        }

        function date_cal(skip) {
            //날짜계산
            let date = new Date();
            //어제, 오늘
            if (skip == 1 || skip == 0) {
                date.setDate(date.getDate() - skip);
                var temp = date.toLocaleString().replaceAll(" ", "").split(".");
                var startdate = temp[0] + "-" + temp[1] + "-" + temp[2];
                lastdate = startdate
            }
            //한달 세달
            else if (skip == 11 || skip == 33 || skip == 66) {
                skip = skip % 10
                //오늘
                date.setDate(date.getDate());
                var temp = date.toLocaleString().replaceAll(" ", "").split(".");
                var lastdate = temp[0] + "-" + temp[1] + "-" + temp[2];

                //계산
                date.setMonth(date.getMonth() - skip);
                var temp = date.toLocaleString().replaceAll(" ", "").split(".");
                var startdate = temp[0] + "-" + temp[1] + "-" + temp[2];
            }
            //특정날짜
            else if (skip == 999) {
            }
            //그외
            else {
                //오늘
                date.setDate(date.getDate());
                var temp = date.toLocaleString().replaceAll(" ", "").split(".");
                var lastdate = temp[0] + "-" + temp[1] + "-" + temp[2];

                //계산
                skip = skip - 1
                date.setDate(date.getDate() - skip);
                var temp = date.toLocaleString().replaceAll(" ", "").split(".");
                var startdate = temp[0] + "-" + temp[1] + "-" + temp[2];
            }

            //
            if (skip != 999) {
                var startDate = startdate;
                var lastDate = lastdate;
            }
            else {
                var startDate = document.querySelector("#input_start").value;
                var lastDate = document.querySelector("#input_end").value;
                document.getElementById('input_start').value = "";
                document.getElementById('input_end').value = "";
            }

            //date마지막 정리
            temp = startDate.split("-")
            if (temp[1].length == 1) { temp[1] = "0" + temp[1] };
            if (temp[2].length == 1) { temp[2] = "0" + temp[2] };
            var startDate = temp[0] + "-" + temp[1] + "-" + temp[2];

            temp = lastDate.split("-")
            if (temp[1].length == 1) { temp[1] = "0" + temp[1] };
            if (temp[2].length == 1) { temp[2] = "0" + temp[2] };
            var lastDate = temp[0] + "-" + temp[1] + "-" + temp[2];
            // console.log(startDate);
            // console.log(lastDate);

            //날짜계산
            function getDatesStartToLast(startDate, lastDate, filter_date) {
                var regex = RegExp(/^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/);
                if (!(regex.test(startDate) && regex.test(lastDate))) return "Not Date Format";
                var result = "";
                var curDate = new Date(startDate);
                while (curDate <= new Date(lastDate)) {
                    filter_date.push(curDate.toISOString().split("T")[0])
                    curDate.setDate(curDate.getDate() + 1);
                }
            }
            var filter_date = new Array;
            getDatesStartToLast(startDate, lastDate, filter_date);
            //console.log(filter_date);
            return filter_date
        }









        //window.onload
        function inni(skip) {
            var filter_cp = ''
            if (typeof skip === "undefined") {
                var filter_date = date_cal(0)
                main('none', skip, filter_date, filter_cp)
            }
            //그 외
            else {
                filter_date = date_cal(skip)
                main('none', skip, filter_date, filter_cp)
            }
        }

        inni(0)
    </script>

</body>

</html>
