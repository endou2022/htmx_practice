SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `sightseeing` (
  `ID` int(10) UNSIGNED NOT NULL,
  `都道府県名` varchar(10) NOT NULL,
  `市区町村名` varchar(50) NOT NULL,
  `名称` varchar(100) NOT NULL,
  `名称_カナ` varchar(200) NOT NULL,
  `住所` varchar(200) NOT NULL,
  `説明` varchar(500) NOT NULL,
  `URL` varchar(200) NOT NULL,
  `備考` varchar(500) NOT NULL,
  `登録日` date NOT NULL DEFAULT current_timestamp(),
  `更新日時` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `更新回数` int(10) UNSIGNED NOT NULL DEFAULT 0
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='高山市の観光施設：オープンデータ';

TRUNCATE TABLE `sightseeing`;
INSERT INTO `sightseeing` (`ID`, `都道府県名`, `市区町村名`, `名称`, `名称_カナ`, `住所`, `説明`, `URL`, `備考`) VALUES
(1, '岐阜県', '高山市', '飛騨民俗村', 'ヒダミンゾクムラ', '高山市上岡本町1丁目590番地', '野外博物館', '', ''),
(2, '岐阜県', '高山市', '飛騨高山観光案内所', 'ヒダタカヤマカンコウアンナイショ', '高山市花里町5丁目51番地', '観光案内所', '', ''),
(3, '岐阜県', '高山市', '乗鞍高原飛騨高山キャンプ場', 'ノリクラコウゲンヒダタカヤマキャンプジョウ', '高山市岩井町910番地1', 'キャンプ場', '', ''),
(4, '岐阜県', '高山市', '乗鞍高原飛騨高山スキー場', 'ノリクラコウゲンヒダタカヤマスキージョウ', '高山市岩井町910番地1', 'スキー場', '', ''),
(5, '岐阜県', '高山市', '岩舟河川公園', 'イワフネカセンコウエン', '高山市丹生川町柏原359番地1', 'キャンプ場、コテージ', '', ''),
(6, '岐阜県', '高山市', '乗鞍バスターミナル', 'ノリクラバスターミナル', '高山市丹生川町岩井谷1223番地', 'バス待合所、レストラン、売店、トイレ', '', ''),
(7, '岐阜県', '高山市', '朴の木平駐車場', 'ホオノキダイラチュウシャジョウ', '高山市丹生川町久手465番地1', 'バス待合所、トイレ', '', ''),
(8, '岐阜県', '高山市', 'ジョイフル朴の木', 'ジョイフルホオノキ', '高山市丹生川町久手447番地', '宿泊施設、日帰り入浴施設、レストラン', '', ''),
(9, '岐阜県', '高山市', 'ひだ清見ラベンダー公園', 'ヒダキヨミラベンダーコウエン', '高山市清見町三日町2431番地', '花園', '', ''),
(10, '岐阜県', '高山市', 'パスカル清見', 'パスカルキヨミ', '高山市清見町大原801番地2', 'キャンプ場、芝生広場、トイレ', '', ''),
(11, '岐阜県', '高山市', '森林公園大倉滝', 'シンリンコウエンオオクラダキ', '高山市清見町坂下981番地1', 'レストラン、コテージ、トイレ', '', ''),
(12, '岐阜県', '高山市', 'そばの里荘川', 'ソバノサトショウカワ', '高山市荘川町中畑61番地', 'レストラン、貸館、遊歩道', '', ''),
(13, '岐阜県', '高山市', '荘川の里', 'ショウカワノサト', '高山市荘川町新渕53番地', '野外博物館', '', ''),
(14, '岐阜県', '高山市', '桜香の湯', 'オウカノユ', '高山市荘川町猿丸87番地', '日帰り入浴施設、レストラン', '', ''),
(15, '岐阜県', '高山市', 'みぼろ湖オートキャンプサイト', 'ミボロコオートキャンプサイト', '高山市荘川町中野262番地1', 'キャンプ場', '', ''),
(16, '岐阜県', '高山市', 'モンデウス飛騨位山スノーパーク', 'モンデウスヒダクライヤマスノーパーク', '高山市一之宮町7846番地1', 'スキー場', '', ''),
(17, '岐阜県', '高山市', '飛騨舟山スノーリゾートアルコピア', 'ヒダフナヤマスノーリゾートアルコピア', '高山市久々野町無数河4141番地', 'スキー場', '', ''),
(18, '岐阜県', '高山市', '胡桃島キャンプ場', 'クルミジマキャンプジョウ', '高山市朝日町胡桃島1251番地', 'キャンプ場、コテージ', '', ''),
(19, '岐阜県', '高山市', '野麦峠お助け小屋', 'ノムギトウゲオタスケゴヤ', '高山市高根町野麦592番地', 'レストラン、トイレ', '', ''),
(20, '岐阜県', '高山市', '野麦オートビレッジ', 'ノムギオートビレッジ', '高山市高根町野麦660番地1', 'キャンプ場', '', ''),
(21, '岐阜県', '高山市', '塩沢温泉七峰館', 'シオザワオンセンシチホウカン', '高山市高根町上ケ洞290番地', '宿泊施設、日帰り入浴施設、レストラン', '', ''),
(22, '岐阜県', '高山市', 'しぶきの湯遊湯館', 'シブキノユユウユカン', '高山市国府町宇津江964番地', '日帰り入浴施設、レストラン', '', ''),
(23, '岐阜県', '高山市', '四十八滝公園', 'シジュウハチタキコウエン', '高山市国府町宇津江3235番地86', 'キャンプ場、コテージ、レストラン、遊歩道、花園', '', ''),
(24, '岐阜県', '高山市', '新穂高センター', 'シンホタカセンター', '高山市奥飛騨温泉郷神坂710番地9', '観光案内所、トイレ', '', ''),
(25, '岐阜県', '高山市', '新穂高駐車場', 'シンホタカチュウシャジョウ', '高山市奥飛騨温泉郷神坂710番地10', '有料駐車場', '', ''),
(26, '岐阜県', '高山市', 'あかんだな駐車場', 'アカンダナチュウシャジョウ', '高山市奥飛騨温泉郷平湯791番地38', '有料駐車場、バス待合所', '', '');


ALTER TABLE `sightseeing`
  ADD PRIMARY KEY (`ID`);


ALTER TABLE `sightseeing`
  MODIFY `ID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;